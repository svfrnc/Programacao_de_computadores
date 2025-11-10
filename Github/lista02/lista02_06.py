DistanciaAB=int(input())
VelocidadeAB=int(input())
Tempo_percurso=DistanciaAB//VelocidadeAB
Total_percurso=DistanciaAB/VelocidadeAB
minutos=int((Total_percurso-Tempo_percurso) * 60) 
print(f'{Tempo_percurso:02d}:{minutos:02d}')
