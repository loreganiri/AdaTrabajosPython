Empresa = { 
    'Nombre_empresa':'Ratrace',
    'Empleados':
    [
        { 'Id_empleado': 101,'Nombre1':'Lana Williams' ,'Departamento' : 'PR','Salario':4000},
        {'Id_empleado': 102,'Nombre2':'Mike Adams' ,'Departamento' : 'Development','Salario':5000},
        {'Id_empleado': 103,'Nombre3':'Jose Luis Flores' ,'Departamento' : 'Management','Salario':3000},
    ]

}
print("Escriba el Id del empleado (101, 102, 103,104) : ")
Id = int(input())
if Id == 101:
    print (Empresa['Empleados'][0])
    print("¿Cual es el salario nuevo?")
    x=input()
    Empresa['Empleados'][0]['Salario']=x
    print (Empresa['Empleados'][0])
else:
    if Id == 102:
        print (Empresa['Empleados'][1])
        print("¿Cual es el salario nuevo?")
        x=input()
        Empresa['Empleados'][1]['Salario']=x
        print (Empresa['Empleados'][1])
    else:
        if Id == 103:
            print (Empresa['Empleados'][2])
            print("¿Cual es el salario nuevo?")
            x=input()
            Empresa['Empleados'][2]['Salario']=x
            print (Empresa['Empleados'][2])
        else:
            print (Empresa['Empleados'][3])
        print("¿Cual es el salario nuevo?")
        x=input()
        Empresa['Empleados'][3]['Salario']=x
        print (Empresa['Empleados'][3])