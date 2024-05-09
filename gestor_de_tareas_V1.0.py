__autor__ = 'Enrique Manuel Jimenez Secilla'
__version__ = '1.0'

import os
import json


class TaskManager:
    def __init__(self):
        """
        Inicializa el objeto TaskManager.

        Este método crea un diccionario vacío llamado `tasks_dictionary` para almacenar las tareas.

        Parámetros:
            Ninguno

        Retorna:
            Ninguno
        """

        self.tasks_dictionary = dict()

    def clear_screen(self):
        """
        Inicializa el objeto TaskManager.

        Este método crea un diccionario vacío llamado `tasks_dictionary` para almacenar las tareas.

        Parámetros:
            Ninguno

        Retorna:
            Ninguno
        """

        if os.name == 'nt':  # Verificar si estamos en Windows
            os.system('cls')
        else:  # Si no estamos en Windows, asumimos que es un sistema Unix/Linux
            os.system('clear')

    def list_tasks(self):
        """
        Un método que lista todas las tareas, imprime sus nombres y estados, y solicita al usuario que presione ENTER para regresar al menú.
        """

        contador = 0

        print(AMARILLO + '\nListado de Tareas:\n')
        print(BLANCO + 'Nombre de la tarea'.ljust(25), 'Estado de la tarea')
        print(ROJO + '-' * 50)
        for task_name, state in self.tasks_dictionary.items():
            contador += 1
            print(
                f"{ROJO}{contador}. {BLANCO}{task_name.ljust(25)} {ROJO + 'Pendiente' if state == False else VERDE + 'Completada' + BLANCO}")

        input(f'\n{BLANCO}Pulsa {AMARILLO}"ENTER"{BLANCO} para regresar al menu... ')

        self.save_to_file()  # Guardar en el archivo después de mostrar las tareas

    def create_task(self):
        """
        Crea una nueva tarea con el nombre dado y la agrega al diccionario de tareas.

        Parámetros:
            self (TaskManager): El objeto TaskManager.

        Retorna:
            Ninguno
        """

        task_name = input(BLANCO +
                          '\nIntroduce un nombre para la tarea que deseas crear: ' + AMARILLO).capitalize()
        self.tasks_dictionary[task_name] = False
        print(BLANCO + '\nTarea' + AMARILLO +
              f' {task_name}' + BLANCO + ' creada correctamente.')
        input(f'\nPulse {AMARILLO}"ENTER"{BLANCO} para regresar al menu... ')

        self.save_to_file()  # Guardar en el archivo después de crear la tarea

    def update_task(self):
        """
        Actualiza una tarea marcándola como completada.

        Esta función muestra una lista de todas las tareas pendientes y solicita al usuario que ingrese el nombre de la tarea que desea 
        marcar como completada. Si la tarea existe, la marca como completada y guarda los cambios en el archivo. Si no hay tareas 
        pendientes, muestra un mensaje y regresa al menú principal.

        Parámetros:
            self (TaskManager): El objeto TaskManager.

        Devoluciones:
            Ninguno
        """

        print(BLANCO + '\nEste es un listado de todas las tareas pendientes')
        print(ROJO + '-' * 49)

        contador = 0

        for clave, valor in self.tasks_dictionary.items():
            if valor == False:
                contador += 1
                print(ROJO + str(contador) + '.' + BLANCO, clave)

        if contador == 0:
            print(
                BLANCO + '\nNo hay ningura tarea pendiente para marcar como' + VERDE + ' completada.\n')
            input(
                BLANCO + f'\nPulse {AMARILLO}"ENTER"{BLANCO} para regresar al menu... ')
            main(task_manager)

        task_name = input(
            BLANCO + f'\nIntroduce el nombre de la tarea que deseas marcar como completada o pulsa {AMARILLO}"ENTER"{BLANCO} para regresar al Menu Principal: ' + AMARILLO).capitalize()

        if task_name in self.tasks_dictionary:
            self.tasks_dictionary[task_name] = True
            print(
                BLANCO, f'\nTarea {AMARILLO + task_name + BLANCO} marcada como completada.')
        elif task_name == '':
            main(task_manager)
        else:
            print(f'\n{BLANCO}La tarea {AMARILLO + task_name + BLANCO} no existe.')

        input(f'\nPulse {AMARILLO}"ENTER"{BLANCO} para regresar al menu... ')

        self.save_to_file()  # Guardar en el archivo después de actualizar la tarea

    def delete_task(self):
        """
        Elimina una tarea del gestor de tareas.

        Esta función muestra una lista de todas las tareas pendientes y solicita al usuario que ingrese el nombre de la tarea que desea eliminar. 
        Si la tarea existe, se elimina del gestor de tareas y se guarda en el archivo. Si no hay tareas pendientes, se muestra un mensaje y el 
        usuario se devuelve al menú principal.

        Parámetros:
            self (TaskManager): El objeto TaskManager.

        Retorna:
            Ninguno
        """

        contador = 0

        print(AMARILLO + '\nListado de Tareas:\n')
        print(BLANCO + 'Nombre de la tarea'.ljust(25), 'Estado de la tarea')
        print(AMARILLO + '-' * 50)

        for task_name, state in self.tasks_dictionary.items():
            contador += 1
            print(
                f"{ROJO} {contador}. {BLANCO + task_name.ljust(25)} {ROJO + 'Pendiente' if state == False else VERDE + 'Completada' + BLANCO}")

        task_name = input(
            BLANCO + f'\nIntroduce el nombre de la tarea a eliminar o pulse {AMARILLO}"ENTER" {BLANCO}para regresar de nuevo al Menu Principal: ' + AMARILLO).capitalize()

        if task_name in self.tasks_dictionary:
            del self.tasks_dictionary[task_name]
            print(
                f"\n{BLANCO}Tarea {AMARILLO + task_name + BLANCO} eliminada correctamente.")
        elif task_name == '':
            main(task_manager)

        else:
            print(f"\nLa tarea {AMARILLO + task_name + BLANCO} no existe.")

        input(f'\nPulse {AMARILLO}"ENTER"{BLANCO} para regresar al menu... ')

        self.save_to_file()  # Guardar en el archivo después de eliminar la tarea

    def save_to_file(self):
        """
        Guarda el contenido del diccionario tasks_dictionary en un archivo JSON llamado "data.json".
        """

        with open("data.json", "w") as file:
            json.dump(self.tasks_dictionary, file)


def main(task_manager):
    """
    La función principal del programa, que interactúa con el usuario.

    Esta función muestra continuamente un menú al usuario y le pide que seleccione una opción. 
    Las opciones son:

    - [1] Crear una nueva tarea.
    - [2] Listar todas las tareas.
    - [3] Marcar una tarea como completada.
    - [4] Eliminar una tarea.
    - [5] Salir de la aplicación.

    Se le pide al usuario que ingrese su selección, y la función valida la entrada. 
    Si el usuario selecciona una opción inválida, se le solicita nuevamente hasta que se ingrese una opción válida.

    Dependiendo de la selección del usuario, se llama al método correspondiente del objeto TaskManager.

    Si el usuario selecciona la opción [5], el programa sale.

    Parámetros:
    - task_manager (TaskManager): Una instancia de la clase TaskManager.

    Retorna:
    - Ninguno
    """

    # Función principal para interactuar con el usuario
    while True:
        task_manager.clear_screen()
        print(AMARILLO + """
                    __                    __        __                            
   ____ ____  _____/ /_____  _____   ____/ /__     / /_____ _________  ____ ______
  / __ `/ _ \/ ___/ __/ __ \/ ___/  / __  / _ \   / __/ __ `/ ___/ _ \/ __ `/ ___/
 / /_/ /  __(__  ) /_/ /_/ / /     / /_/ /  __/  / /_/ /_/ / /  /  __/ /_/ (__  ) 
 \__, /\___/____/\__/\____/_/      \__,_/\___/   \__/\__,_/_/   \___/\__,_/____/  
/____/                                                                            

              """)

        print(CYAN + 'Realizado por Enrique M. Jimenez\n')
        print(AMARILLO + '\nMENU PRINCIPAL')
        print(ROJO + '-' * 14)
        print('\n')
        print(ROJO + '[1]' + AZUL + ' Crear una tarea nueva.')
        print(ROJO + '[2]' + AZUL + ' Listar todas las tareas.')
        print(ROJO + '[3]' + AZUL + ' Marcar una tarea como completada.')
        print(ROJO + '[4]' + AZUL + ' Eliminar una tarea.')
        print(ROJO + '[5]' + AZUL + ' Salir de la aplicacion.')

        option = input(BLANCO
                       + '\nSelecciona una opción: ' + AMARILLO)

        while option not in ['1', '2', '3', '4', '5']:
            print(VERDE + '\nOpción no válida. Selecciona una opción del menú.')
            option = input(BLANCO + '\nSelecciona una opción: ' + AMARILLO)

        if option == '1':
            task_manager.create_task()
        elif option == '2':
            task_manager.list_tasks()
        elif option == '3':
            task_manager.update_task()
        elif option == '4':
            task_manager.delete_task()
        elif option == '5':
            print(VERDE + '\nSaliendo de la aplicacion... Hasta pronto!!')
            exit()


# Codigos de colores Acsii
ROJO = '\033[31m'
VERDE = '\033[32m'
AMARILLO = '\033[33m'
AZUL = '\033[34m'
CYAN = '\033[36m'
BLANCO = '\033[37m'

# Creamos una instancia de la clase TaskManager
task_manager = TaskManager()

# Asignamos la ruta al archivo JSON
file_path = "data.json"

# Llamamos a la función para limpiar la pantalla
task_manager.clear_screen()

# Creamos si no existe o cargamos el diccionario de tareas desde el archivo JSON
try:
    if os.path.isfile(file_path):
        print(
            f'Para iniciar el programa se necesita crear o cargar un fichero {AMARILLO}JSON{BLANCO}, el archivo ya existe en el sistema, se procedera a la carga de datos...\n ')
        with open(file_path, "r") as file:
            # Cargamos las tareas desde el archivo JSON
            task_manager.tasks_dictionary = json.load(file)
            input(f'Pulse {AMARILLO}ENTER{BLANCO} para continuar... ')
    else:
        print(
            f'Para iniciar el programa se necesita crear o cargar un fichero {AMARILLO}JSON{BLANCO}, el archivo no existe. Se creará uno nuevo...')
        # Creamos un archivo nuevo y lo inicializamos con un diccionario vacío
        with open(file_path, "w") as file:
            json.dump({}, file)
        input(
            f'Fichero creado correctamente, pulse {AMARILLO} "ENTER" {BLANCO} para continuar... ')
except Exception as e:
    print(f"Error al cargar el archivo: {e}")


if __name__ == '__main__':
    main(task_manager)
