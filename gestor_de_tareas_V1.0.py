__autor__ = 'Enrique Manuel Jimenez Secilla'
__version__ = '1.0'

import os
import json


class TaskManager:
    def __init__(self):
        """
        Inicializa el objeto TaskManager con un diccionario vacío para almacenar las tareas.

        Este método se ejecuta al crear una instancia de la clase TaskManager. Inicializa un atributo de instancia llamado `tasks_dictionary` como un diccionario vacío.
        Este diccionario se utilizará para almacenar las tareas agregadas al gestor de tareas.

        Parámetros:
            Ninguno

        Returns:
            None
        """

        self.tasks_dictionary = dict()

    def clear_screen(self):
        """
        Limpia la pantalla de la consola en función del sistema operativo en uso. 

        Si el sistema operativo es Windows, utiliza el comando 'cls' para limpiar la pantalla.
        En caso de que el sistema operativo sea Unix/Linux, utiliza el comando 'clear'.

        Parámetros
        ----------
        self : clase
            La instancia de la clase a la que pertenece el método

        Returns
        -------
        None
        """

        if os.name == 'nt':  # Verificar si estamos en Windows
            os.system('cls')
        else:  # Si no estamos en Windows, asumimos que es un sistema Unix/Linux
            os.system('clear')

    def list_tasks(self):
        """
        Muestra un listado de todas las tareas junto con su estado, e imprime el resultado en la consola.

        El método recorre el diccionario de tareas y muestra una tabla con los nombres de las tareas y sus estados (completadas o pendientes).
        Los colores se usan para resaltar la información y mejorar la legibilidad.

        Parámetros
        ----------
        self : clase
            La instancia de la clase a la que pertenece el método

        Returns
        -------
        None
        """

        contador = 0  # Inicializa un contador para numerar las tareas

        print(AMARILLO + '\nListado de Tareas:\n')
        print(BLANCO + 'Nombre de la tarea'.ljust(25), 'Estado de la tarea')
        print(ROJO + '-' * 50)

        # Recorre las tareas en el diccionario de tareas
        for task_name, state in self.tasks_dictionary.items():
            contador += 1
            print(
                f"{ROJO}{contador}. {BLANCO}{task_name.ljust(25)} {ROJO + 'Pendiente' if state == False else VERDE + 'Completada' + BLANCO}")

        input(f'\n{BLANCO}Pulsa {AMARILLO}"ENTER"{
              BLANCO} para regresar al menu... ')

        self.save_to_file()  # Guardar en el archivo después de mostrar las tareas

    def create_task(self):
        """
        Permite al usuario crear una nueva tarea y agregarla al diccionario de tareas del objeto TaskManager.

        El método solicita al usuario que ingrese un nombre para la nueva tarea y la agrega al diccionario de tareas con un estado inicial 'False' (pendiente).
        Después, se muestra un mensaje de confirmación y se actualiza el archivo con la tarea recién agregada.

        Parámetros:
            self (TaskManager): La instancia del objeto TaskManager a la que se agregará la nueva tarea.

        Returns:
            None
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

        contador = 0  # Inicializa un contador para numerar las tareas pendientes

        for clave, valor in self.tasks_dictionary.items():  # Recorre las tareas en el diccionario de tareas
            if valor == False:  # Si la tarea está pendiente
                contador += 1  # Incrementa el contador de tareas pendientes
                print(ROJO + str(contador) + '.' + BLANCO, clave)

        if contador == 0:  # Si no hay tareas pendientes
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
            print(f'\n{BLANCO}La tarea {
                  AMARILLO + task_name + BLANCO} no existe.')

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

        contador = 0  # Inicializa un contador para enumerar las tareas

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
            # Si el usuario presiona Enter, vuelve al Menú Principal
            main(task_manager)

        else:
            print(f"\nLa tarea {AMARILLO + task_name + BLANCO} no existe.")

        input(f'\nPulse {AMARILLO}"ENTER"{BLANCO} para regresar al menu... ')

        self.save_to_file()  # Guardar en el archivo después de eliminar la tarea

    def save_to_file(self):
        """
        Guarda el diccionario de tareas (`tasks_dictionary`) del objeto TaskManager en un archivo JSON llamado "data.json".

        Este método serializa el diccionario de tareas como JSON y lo almacena en el archivo "data.json". Cualquier actualización realizada en el diccionario de tareas se reflejará en el archivo JSON después de llamar a este método.

        Parámetros:
            self (TaskManager): La instancia del objeto TaskManager cuyas tareas se guardarán en el archivo JSON.

        Returns:
            None
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
        # Muestra las opciones del menú con sus respectivos números de opción
        print(ROJO + '[1]' + AZUL + ' Crear una tarea nueva.')
        print(ROJO + '[2]' + AZUL + ' Listar todas las tareas.')
        print(ROJO + '[3]' + AZUL + ' Marcar una tarea como completada.')
        print(ROJO + '[4]' + AZUL + ' Eliminar una tarea.')
        print(ROJO + '[5]' + AZUL + ' Salir de la aplicacion.')

        option = input(BLANCO
                       + '\nSelecciona una opción: ' + AMARILLO)

        # Verifica que la opción seleccionada esté dentro del rango de opciones válidas
        while option not in ['1', '2', '3', '4', '5']:
            print(VERDE + '\nOpción no válida. Selecciona una opción del menú.')
            option = input(BLANCO + '\nSelecciona una opción: ' + AMARILLO)

        # Ejecuta la acción correspondiente según la opción seleccionada por el usuario
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
    print(f'Error al cargar el archivo: {e}')


if __name__ == '__main__':
    main(task_manager)
