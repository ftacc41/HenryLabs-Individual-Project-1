from fastapi import FastAPI
import pandas as pd

app = FastAPI()

@app.get('/')
async def read_root():
    return {'Primera API'}


#read csv into global variable in order to run querys
@app.on_event('startup')
def startup():
    global content
    content = pd.read_csv('content_global.csv', encoding='utf-8')


#function that returns title of longest movie or tvshow on a certain platform in a specific year (release date)
@app.get('/get_max_duration({anio,plataforma, lentype})')   
def get_max_duration(anio:int,plataforma:str,lentype:str):
    temp_df=content[(content['release_year']==anio) & (content['platform']==plataforma)]
    if lentype == 'min':
        time=temp_df.movie_duration_mins.max()
        title=temp_df[temp_df.movie_duration_mins==time] ['title']
        title=title.to_list()
        title=title[0]
    elif lentype == 'seasons':
        time=temp_df.seasons.max()
        title=temp_df[temp_df.seasons==time] ['title']
        title=title.to_list()
        title=title[0]
    return title


#function for retreiving both movie and tv show count (seperatly) for a certain platform
@app.get('/get_count_plataform({platforma})')   
def get_count_plataforma (plataforma:str):
    res1=((content['platform']==plataforma) & (content['type'].str.contains('Movie'))).sum()
    res2=((content['platform']==plataforma) & (content['type'].str.contains('TV Show'))).sum()
    return  ( str(plataforma)+ " has "+str(res1)+ ' movies and ' +str(res2)+ ' tv shows')
   


#function that returns the amount of times a certain genre appears and what platform that corresponds to
@app.get('/get_listedin({genero})')
def get_listedin (genero):
    result1 = ((content['listed_in'].str.contains(genero)) &(content['platform']== 'amazon prime')).sum()
    result2 = ((content['listed_in'].str.contains(genero)) &(content['platform']== 'netflix')).sum()
    result3 = ((content['listed_in'].str.contains(genero)) &(content['platform']== 'hulu')).sum()
    result4 = ((content['listed_in'].str.contains(genero)) &(content['platform']== 'disney plus')).sum()
        
    data = [[result1, 'amazon prime'], [result2, 'netflix'], [result3, 'hulu'], [result4, 'disney plus']]
    df = pd.DataFrame(data, columns= ['result', 'platform'])
    final_df = df.sort_values(by=['result'], ascending=False)
    x = final_df.loc[[0]]
    x = x.to_numpy()
    x = list(x)[0]
    return str(x)


    
    

#
@app.get('/get_actor({plataforma},{anio})')
def get_actor(plataforma,año):
    
    plataforma=str(plataforma.lower())
    año=int(año)

    df_plataforma=(content[(content.platform==plataforma)&(content.release_year==año)&(content.cast!='no data')])
    df_plataforma['cast']=df_plataforma['cast'].replace(' ,',',') 
    df_plataforma['cast']=df_plataforma['cast'].replace(', ',',') 

    lista_actores_unicos=[]

    for lista in df_plataforma['cast']:
        lista=str(lista).split(',')
        for actor in lista:
            actor=actor.strip()
            lista_actores_unicos.append(actor)
    lista_actores_unicos=list(set(lista_actores_unicos))

    lista_actores=[]
    lista_repetidos=[]
    dicc=dict()

    for lista in df_plataforma['cast']:
        lista=str(lista).split(',')
        for actor in lista:
            actor=actor.strip()
            lista_actores.append(actor)
    lista_actores_unicos=list(set(lista_actores))

    for i,e in enumerate(lista_actores):
        contador=lista_actores.count(e)
        dicc[e]=contador
    
    a=max(dicc, key=dicc.get)

    m=dicc.get(a)
    rta= str(a) + ' ' +str(m)
    return rta