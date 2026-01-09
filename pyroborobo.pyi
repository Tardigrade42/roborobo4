from __future__ import annotations
import collections.abc
import numpy
import numpy.typing
import typing
__all__: list[str] = ['AgentObserver', 'CircleObject', 'Controller', 'DistAwareController', 'Landmark', 'MovableObject', 'PhysicalObject', 'PyHandleFastVector', 'PyObjectFastVector', 'Pyroborobo', 'RoboroboSurface', 'Robot', 'SquareObject', 'World', 'WorldModel', 'WorldObserver']
class AgentObserver:
    def __init__(self, world_model: WorldModel) -> None:
        ...
    def reset(self) -> None:
        """
        Reset the agent observer
        """
    def step_post(self) -> None:
        """
        Called at each timestep after the agent's controller.
        """
    def step_pre(self) -> None:
        """
        Called at each timestep before the agent's controller.
        """
    @property
    def controller(self) -> Controller:
        """
        Controller: Controller associated with this AgentObserver
        """
    @property
    def world_model(self) -> WorldModel:
        """
        WorldModel: WorldModel associated with this AgentObserver
        """
class CircleObject(PhysicalObject):
    """
    
    CircleObject(id: int, data: dict) -> CircleObject
    
    Physical object with a circular shape
    
    Read :doc:`/tuto/objects` for a tutorial on how to use Objects.
    
    Parameters
    ----------
    id: int
        The id of the object
    data: dict (optional)
        The data for the object read from the properties file
    
    See also
    --------
    PhysicalObject: Reference for physical objects
    
    
    """
    @typing.overload
    def __init__(self, id: typing.SupportsInt = -1) -> None:
        ...
    @typing.overload
    def __init__(self, id: typing.SupportsInt = -1, data: dict = {}) -> None:
        ...
    def can_register(self) -> bool:
        """
        Can the object be registered at its current location
        
        Returns
        -------
        bool: Can the object be registered at its current location
        """
    def hide(self) -> None:
        """
        Hide the object (collision can be still active)
        """
    def is_pushed(self, id: typing.SupportsInt, speed: tuple[typing.SupportsFloat, typing.SupportsFloat]) -> None:
        """
        Callback when the object is pushed
        
        Parameters
        ----------
        id: int
            The id of the robot that has pushed the object
        speed: tuple(double, double)
            The speed at which the robot pushed the object
        """
    def is_touched(self, id: typing.SupportsInt) -> None:
        """
        Callback when the object is touched
        
        Parameters
        ----------
        id: int
            The id of the robot that has touched the object
        """
    def is_walked(self, id: typing.SupportsInt) -> None:
        """
        Callback when the object is walked on
        
        Parameters
        ----------
        id: int
            The id of the robot that has walked on the object
        """
    def register(self) -> None:
        """
        Register the object (activate collision)
        """
    def set_color(self, red: typing.SupportsInt, blue: typing.SupportsInt, green: typing.SupportsInt) -> None:
        """
        Set the color (r,g,b) of the object
        
        Parameters
        ----------
        red: int
            The red component of the color in [0, 255]
        blue: int
            The blue component of the color in [0, 255]
        green: int
            The green component of the color in [0, 255]
        """
    def set_footprint_radius(self, radius: typing.SupportsFloat, force: bool = False) -> None:
        """
        set the footprint radius of the circle in pixel. if force is true, no check about the object being unregistered is done.
        """
    def set_radius(self, radius: typing.SupportsFloat, force: bool = False) -> None:
        """
        set the radius of the circle in pixel. if force is true, no check about the object being unregistered is done.
        """
    def show(self) -> None:
        """
        Show the object (collision can be still inactive)
        """
    def step(self) -> None:
        """
        called at each timestep
        """
    def unregister(self) -> None:
        """
        Unregister the object (deactivate collision)
        """
    @property
    def footprint_radius(self) -> float:
        """
        float: The radius of the footprint of the circle
        """
    @footprint_radius.setter
    def footprint_radius(self, arg1: typing.SupportsInt) -> None:
        ...
    @property
    def id(self) -> int:
        """
        int: the id of the object
        """
    @property
    def radius(self) -> float:
        """
        float: The radius of the hard part of the circle
        """
    @radius.setter
    def radius(self, arg1: typing.SupportsInt) -> None:
        ...
class Controller:
    """
    
    Class to extend a Roborobo Controller in python.
    
    .. warning::
        If the __init__ is overridden, it is absolutely necessary to call the PyController constructor by doing :
    
        .. code-block:: python
    
            def __init__(self, world_model):
                PyController.__init__(self, world_model)
    
        Not doing so leads to cryptic errors due to the interface between python and c++.
    
        It is also necessary to override `step` and `reset`. Not doing so leads to cryptic errors.
    
    
    """
    def __init__(self, world_model: RobotWorldModel) -> None:
        ...
    def find_random_location(self) -> None:
        """
        Place the robot at a random location
        """
    def get_all_distances(self) -> numpy.ndarray:
        """
        Return a numpy array of all distances.
        """
    def get_all_object_instances(self) -> PyHandleFastVector:
        """
        Vector[`PhysicalObject`]: A vector of the object instances seen by each sensor, None if no object in sight.
        """
    def get_all_objects(self) -> numpy.ndarray:
        """
        Vector[int]: Id of the object seen by each sensor. -1 if no object in sight
        """
    def get_all_robot_controllers(self) -> PyHandleFastVector:
        """
        Vector[Controller]: Get the robots' controllers seen by all the sensors (None if a sensor has no robot in sight)
        """
    def get_all_robot_ids(self) -> numpy.typing.NDArray[numpy.int32]:
        """
        Return a vector of all the robots id seen for each sensor (-1 if not robot in sight)
        """
    def get_all_robot_relative_orientations(self) -> numpy.typing.NDArray[numpy.float64]:
        """
        Vector[float]: Get the robots' relative orientations compared to self for each sensors
        """
    def get_all_sensor_angles(self) -> numpy.ndarray:
        """
        Return a numpy array of all sensor target angles from the center of the robot in degree.
        """
    def get_all_walls(self) -> numpy.ndarray:
        """
        Vector[`bool`]: Tell if it's a wall seen by each sensor
        """
    def get_closest_landmark_dist(self) -> float:
        """
        float: The distance to the closest landmark
        """
    def get_closest_landmark_orientation(self) -> float:
        """
        float: The orientation to the closest landmark
        """
    def get_distance_at(self, sensor_id: typing.SupportsInt) -> float:
        """
        float: The distance to the object in range [0, 1], if 1, nothing is in sight
        """
    def get_ground_sensor_values(self) -> tuple:
        """
        tuple[float, float, float]: (red, green, blue) from the ground sensor of the robot between [0,1]
        """
    def get_id(self) -> int:
        """
        int: Robot unique ID. (alias of property `id`).
        """
    def get_object_at(self, sensor_id: typing.SupportsInt) -> int:
        """
        Int: Id of the object if seen else -1 for the sensor ``sensor_id``
        """
    def get_object_instance_at(self, sensor_id: typing.SupportsInt) -> typing.Any:
        """
        `PhysicalObject`: The instance of the object seen by ``sensor_id``. None if no object in sight.
        """
    def get_robot_controller_at(self, sensor_id: typing.SupportsInt) -> typing.Any:
        """
        Controller: Get the robot's controller seen by the sensor ``sensor_id``
        """
    def get_robot_id_at(self, sensor_id: typing.SupportsInt) -> int:
        """
        int: Get the robot id of the robot seen by the sensor ``sensor_id``
        """
    def get_robot_relative_orientation_at(self, sensor_id: typing.SupportsInt) -> float:
        """
        float: Get robot's relative orientation compared to self seen by the sensor ``sensor_id``
        """
    def get_sensor_angle_at(self, sensor_id: typing.SupportsInt) -> float:
        """
        float: The angle of the sensor target from the center of the robot in degree
        """
    def get_wall_at(self, sensor_id: typing.SupportsInt) -> int:
        """
        int: Tell if it's a wall seen by the sensor ``sensor_id`` (0 not a wall or 1 for a wall)
        """
    def register(self) -> None:
        """
        Add the robot in the simulation (can collide with others)
        """
    def reset(self) -> None:
        """
        call at the initialization of roborobo
        """
    def set_absolute_orientation(self, arg0: typing.SupportsFloat) -> None:
        """
        set the absolute orientation of the robot
        """
    def set_color(self, arg0: typing.SupportsInt, arg1: typing.SupportsInt, arg2: typing.SupportsInt) -> None:
        """
        Set the color of the robot (r,g,b).
        :param: r int [0, 255]
        :param: g int [0, 255]
        :param: b int [0, 255]
        """
    def set_position(self, x: typing.SupportsFloat, y: typing.SupportsFloat, register: bool = True, force: bool = True) -> bool:
        """
        Set the robot at the position (x, y).
        If ``register`` then the function take care of the registration.
        If ``force`` is true, the function ignore collisions.
        """
    def set_rotation(self, rotation_speed: typing.SupportsFloat) -> None:
        """
        Set the robot rotation speed between [-1, 1]
        """
    def set_translation(self, trans_speed: typing.SupportsFloat) -> None:
        """
        Set the robot translation speed between [-1, 1]
        """
    def step(self) -> None:
        """
        Takes the decision of the robot's next action
        
        You can access the sensors and effectors of the robot by reading and modifying its :attr:`~pyroborobo.Controller.world_model`.
        
        Called at each time step of the simulation.
        
        Examples
        --------
        >>> def step(self):
        ...     distance = self.world_model.camera_pixel_distance
        ...     if np.all(distance < 0.5):
        ...         # Nothing around, we can go forward without turning
        ...         self.world_model.translation = 2
        ...         self.world_model.rotation = 0
        ...     else:
        ...         # There are obstacles, we go around in circles slowly
        ...         self.world_model.translation = 0.5
        ...         self.world_model.rotation = 15
        """
    def unregister(self) -> None:
        """
        Remove the robot from the simulation (cannot collide with other, not shown)
        """
    @property
    def absolute_orientation(self) -> float:
        """
        Float: Absolute orientation of the robot
        """
    @property
    def absolute_position(self) -> tuple[float, float]:
        """
        Tuple[float, float]: Robot's absolute position
        """
    @property
    def id(self) -> int:
        """
        int: Robot unique ID.
        """
    @property
    def nb_sensors(self) -> int:
        """
        int: Number of sensors of the robot
        """
    @property
    def rotation(self) -> float:
        """
        float: the robot's actual rotation speed between [-1, 1]
        """
    @property
    def translation(self) -> float:
        """
        float: the robot's actual translation speed between [-1, 1]
        """
    @property
    def world_model(self) -> WorldModel:
        """
        pyroborobo.WorldModel: The robot's world_model
        """
class DistAwareController(Controller):
    def __init__(self, world_model: WorldModel) -> None:
        ...
    def get_distance_to_robot(self, id: typing.SupportsInt) -> float:
        """
        float: The distance to the robot of id ``id``.
        """
class Landmark:
    def __init__(self) -> None:
        """
        Create a Landmark
        """
    def get_coordinates(self) -> tuple[int, int]:
        """
        return the (x,y) coordinates of the landmark.
        """
    def hide(self) -> None:
        """
        Hide the landmark (but do not deactivate it)
        """
    def set_coordinates(self, x: typing.SupportsInt, y: typing.SupportsInt) -> None:
        """
        Set the landmark at the coordinate (x,y)
        """
    def show(self) -> None:
        """
        Show the landmark on screen.
        """
    def step(self) -> None:
        """
        Called at each time step
        """
    @property
    def radius(self) -> float:
        """
        The radius of the landmark
        """
    @radius.setter
    def radius(self, arg1: typing.SupportsFloat) -> None:
        ...
    @property
    def visible(self) -> bool:
        """
        Bool: is the landmark visible (readonly)
        """
class MovableObject(CircleObject):
    def __init__(self, id: typing.SupportsInt = -1) -> None:
        ...
class PhysicalObject:
    """
    
    Abstract Base Class for all roborobo physical objects.
    
    A Physical object is a element in the roborobo simulator with a shape, it can move, disappear, and impact other
    objects or robots. Objects have several callbacks that are called by roborobo.
    
    Objects, once created, always exist in the roborobo simulator. Robots and other objects can interact with them if the
    objects are *registered*. When an object is registered, that means that the simulator takes its physics into account.
    
    Being registered is different from being visible. An object can be made visible (to the human) using the
    :meth:`show` method, or invisible using the :meth:`hide`. If an object is visible and unregistered, it will be visible
    to the humans but robot will *not* see them or collide with them. If an object is invisible and registered, the robots
    will see them and collide with them but the object will not be rendered on the window or screenshot.
    
    You can force roborobo to display all registered elements using the X-ray mode. You can activate the x-ray mode by
    pressing :kbd:`x` on your keyboard when roborobo is rendered in a GUI.
    
    The :meth:`step` method is called at each time step before the robots' step method. The callback :meth:`is_touched`
    is called when a robot has the
    object in sight, :meth:`is_walked` is called when a robot walk on the "soft" surface of the object, and the method
    :meth:`is_pushed` is called when a robot collide with the object.
    
    PhysicalObject cannot be instantiated by itself, only its subclasses :class:`SquareObject` and
    :class:`CircleObject` and their subclasses can be created.
    
    Read :doc:`/tuto/objects` for a tutorial on how to use Objects.
    
    """
    def __init__(self, id: typing.SupportsInt = -1) -> None:
        ...
    def can_register(self) -> bool:
        """
        Can the object be register at its position
        
        Returns
        -------
        bool: can object register at its actual position
        """
    def get_id(self) -> int:
        """
        int: the unique ID of the object. (alias of property `id`).
        """
    def hide(self) -> None:
        """
        hide the object from the screen (collision is still active)
        """
    def is_pushed(self, arg0: typing.SupportsInt, arg1: tuple[typing.SupportsFloat, typing.SupportsFloat]) -> None:
        """
        Triggered when the object is pushed
        """
    def is_registered(self) -> bool:
        """
        Is the object registered
        """
    def is_touched(self, arg0: typing.SupportsInt) -> None:
        """
        Triggered when the object is touched
        """
    def is_walked(self, arg0: typing.SupportsInt) -> None:
        """
        Triggered when the object is walked on
        """
    def register(self) -> None:
        """
        register the object
        """
    def relocate(self) -> None:
        """
        find a random location for the object
        """
    def set_color(self, red: typing.SupportsInt, blue: typing.SupportsInt, green: typing.SupportsInt) -> None:
        """
        Set the color (r,g,b) of the object. r [0, 255], g [0, 255], b [0,255]
        """
    def set_coordinates(self, x: typing.SupportsFloat, y: typing.SupportsFloat, force: bool = False, collision_check: bool = True) -> bool:
        """
        relocate at the (x,y) coordinates. if force=True, do not check if the object is registered. If collision_check=False, do not check for collision
        """
    def set_footprint_color(self, red: typing.SupportsInt, blue: typing.SupportsInt, green: typing.SupportsInt) -> None:
        """
        Set the color (r,g,b) of the object's footprint. r [0, 255], g [0, 255], b [0,255]
        """
    def step(self) -> None:
        """
        Call at each timestep
        """
    def unregister(self) -> None:
        """
        unregister the object
        """
    @property
    def id(self) -> int:
        """
        int: the unique ID of the object.
        """
    @property
    def position(self) -> tuple[float, float]:
        """
        Return the position of the object
        """
    @property
    def registered(self) -> bool:
        """
        Is the object registered
        """
class PyHandleFastVector:
    __hash__: typing.ClassVar[None] = None
    def __bool__(self) -> bool:
        """
        Check whether the list is nonempty
        """
    def __contains__(self, x: typing.Any) -> bool:
        """
        Return true the container contains ``x``
        """
    @typing.overload
    def __delitem__(self, arg0: typing.SupportsInt) -> None:
        """
        Delete the list elements at index ``i``
        """
    @typing.overload
    def __delitem__(self, arg0: slice) -> None:
        """
        Delete list elements using a slice object
        """
    def __eq__(self, arg0: PyHandleFastVector) -> bool:
        ...
    @typing.overload
    def __getitem__(self, s: slice) -> PyHandleFastVector:
        """
        Retrieve list elements using a slice object
        """
    @typing.overload
    def __getitem__(self, arg0: typing.SupportsInt) -> typing.Any:
        ...
    @typing.overload
    def __init__(self) -> None:
        ...
    @typing.overload
    def __init__(self, arg0: PyHandleFastVector) -> None:
        """
        Copy constructor
        """
    @typing.overload
    def __init__(self, arg0: collections.abc.Iterable) -> None:
        ...
    def __iter__(self) -> collections.abc.Iterator[typing.Any]:
        ...
    def __len__(self) -> int:
        ...
    def __ne__(self, arg0: PyHandleFastVector) -> bool:
        ...
    def __repr__(self) -> str:
        """
        Return the canonical string representation of this list.
        """
    @typing.overload
    def __setitem__(self, arg0: typing.SupportsInt, arg1: typing.Any) -> None:
        ...
    @typing.overload
    def __setitem__(self, arg0: slice, arg1: PyHandleFastVector) -> None:
        """
        Assign list elements using a slice object
        """
    def append(self, x: typing.Any) -> None:
        """
        Add an item to the end of the list
        """
    def clear(self) -> None:
        """
        Clear the contents
        """
    def count(self, x: typing.Any) -> int:
        """
        Return the number of times ``x`` appears in the list
        """
    @typing.overload
    def extend(self, L: PyHandleFastVector) -> None:
        """
        Extend the list by appending all the items in the given list
        """
    @typing.overload
    def extend(self, L: collections.abc.Iterable) -> None:
        """
        Extend the list by appending all the items in the given list
        """
    def insert(self, i: typing.SupportsInt, x: typing.Any) -> None:
        """
        Insert an item at a given position.
        """
    @typing.overload
    def pop(self) -> typing.Any:
        """
        Remove and return the last item
        """
    @typing.overload
    def pop(self, i: typing.SupportsInt) -> typing.Any:
        """
        Remove and return the item at index ``i``
        """
    def remove(self, x: typing.Any) -> None:
        """
        Remove the first item from the list whose value is x. It is an error if there is no such item.
        """
class PyObjectFastVector:
    __hash__: typing.ClassVar[None] = None
    def __bool__(self) -> bool:
        """
        Check whether the list is nonempty
        """
    def __contains__(self, x: typing.Any) -> bool:
        """
        Return true the container contains ``x``
        """
    @typing.overload
    def __delitem__(self, arg0: typing.SupportsInt) -> None:
        """
        Delete the list elements at index ``i``
        """
    @typing.overload
    def __delitem__(self, arg0: slice) -> None:
        """
        Delete list elements using a slice object
        """
    def __eq__(self, arg0: PyObjectFastVector) -> bool:
        ...
    @typing.overload
    def __getitem__(self, s: slice) -> PyObjectFastVector:
        """
        Retrieve list elements using a slice object
        """
    @typing.overload
    def __getitem__(self, arg0: typing.SupportsInt) -> typing.Any:
        ...
    @typing.overload
    def __init__(self) -> None:
        ...
    @typing.overload
    def __init__(self, arg0: PyObjectFastVector) -> None:
        """
        Copy constructor
        """
    @typing.overload
    def __init__(self, arg0: collections.abc.Iterable) -> None:
        ...
    def __iter__(self) -> collections.abc.Iterator[typing.Any]:
        ...
    def __len__(self) -> int:
        ...
    def __ne__(self, arg0: PyObjectFastVector) -> bool:
        ...
    def __repr__(self) -> str:
        """
        Return the canonical string representation of this list.
        """
    @typing.overload
    def __setitem__(self, arg0: typing.SupportsInt, arg1: typing.Any) -> None:
        ...
    @typing.overload
    def __setitem__(self, arg0: slice, arg1: PyObjectFastVector) -> None:
        """
        Assign list elements using a slice object
        """
    def append(self, x: typing.Any) -> None:
        """
        Add an item to the end of the list
        """
    def clear(self) -> None:
        """
        Clear the contents
        """
    def count(self, x: typing.Any) -> int:
        """
        Return the number of times ``x`` appears in the list
        """
    @typing.overload
    def extend(self, L: PyObjectFastVector) -> None:
        """
        Extend the list by appending all the items in the given list
        """
    @typing.overload
    def extend(self, L: collections.abc.Iterable) -> None:
        """
        Extend the list by appending all the items in the given list
        """
    def insert(self, i: typing.SupportsInt, x: typing.Any) -> None:
        """
        Insert an item at a given position.
        """
    @typing.overload
    def pop(self) -> typing.Any:
        """
        Remove and return the last item
        """
    @typing.overload
    def pop(self, i: typing.SupportsInt) -> typing.Any:
        """
        Remove and return the item at index ``i``
        """
    def remove(self, x: typing.Any) -> None:
        """
        Remove the first item from the list whose value is x. It is an error if there is no such item.
        """
class Pyroborobo:
    """
    
            Python interface to the roborobo simulator
    
    """
    @staticmethod
    def create(properties_file: str, world_observer_class: typing.Any = None, controller_class: typing.Any = None, world_model_class: typing.Any = None, agent_observer_class: typing.Any = None, object_class_dict: dict = {}, override_conf_dict: dict = {}) -> Pyroborobo:
        """
        Create the singleton Pyroborobo
        
        Parameters
        ----------
        properties_file: str
            Properties file for the roborobo simulator
        
        world_observer_class: Class inherited from PyWorldObserver or str or None
            Class used to instantiate the WorldObserver. It must inherit from :class:`~pyroborobo.PyWorldObserver`.
            It is possible to pass `None`, in which case the C++ class loaded by the loader configuration is used.
            Finally, it is possible to pass the string "dummy", in this case, a minimal class that does not perform any action
            is used.
        
        controller_class: Class inherited from PyController or str or None
            Class used to instantiate the Controllers. It must inherit from :class:`~pyroborobo.PyController`.
            It is possible to pass `None`, in which case the C++ class loaded by the loader configuration is used.
            Finally, it is possible to pass the string "dummy", in this case, a minimal class that does not perform any action
            is used.
        
        world_model_class: Class inherited from PyWorldModel or str or None
            Class used to instantiate the WorldModels. It must inherit from :class:`~pyroborobo.PyWorldModel`.
            It is possible to pass `None`, in which case the C++ class loaded by the loader configuration is used.
            Finally, it is possible to pass the string "dummy", in this case, a minimal class that does not perform any action
            is used.
        
        agent_observer_class: Class inherited from PyAgentObserver or str or None
            Class used to instantiate the AgentObservers. It must inherit from :class:`~pyroborobo.PyAgentObserver`.
            It is possible to pass `None`, in which case the C++ class loaded by the loader configuration is used.
            Finally, it is possible to pass the string "dummy", in this case, a minimal class that does not perform any action
            is used.
        
        object_class_dict: Dict of string -> class inherited from PhysicalObject
            Dict of classes that are used to instantiate physical object from the pytype argument in conf file.
            The classes must be inherited from :class:`pyroborobo.PyCircleObject`, :class:`pyroborobo.PySquareObject` and their subclasses.
        
        override_conf_dict: dict
            Dictionary which updates the configuration file loaded by the ``properties_file`` parameter.
            Dictionary key/value pairs already present in the configuration file are overwritten. Key/value pairs that do not
            exist in the configuration file are added.
        
            DOES NOT WORK YET (dunno why)
        
        Returns
        -------
        pyroborobo.Pyroborobo: The pyroborobo instance
        """
    @staticmethod
    def get() -> Pyroborobo:
        """
        Return the pyroborobo instance
        
        Returns
        -------
        pyroborobo.Pyroborobo
        """
    def add_landmark(self) -> Landmark:
        ...
    def add_object(self, physical_object: typing.Any) -> typing.Any:
        """
        Add a new object to the environment
        """
    def add_robot(self) -> Robot:
        ...
    def close(self) -> None:
        """
        Exit the simulator nicely
        
        Once the simulator is closed, it cannot be reopen in the same python interpreter.
        """
    def get_screen(self) -> RoboroboSurface:
        """
        Return the pyroborobo screen. can be cast into np.array. Still in development.
        """
    def init_trajectory_monitor(self, agent_id: typing.SupportsInt = -1) -> None:
        """
        Monitor the trajectory of all agents (no argument or -1) or of agent with id ``agent_id``. Save the trajectory image with
        ``save_trajectory_image``.
        
        Parameters
        ----------
        
        agent_id : int (default -1)
            If -1, monitor all agents trajectory, else monitor the trajectory of agent with id ``agent_id``.
        """
    @typing.overload
    def is_id_robot(self, id: typing.SupportsInt) -> bool:
        """
        tell if it's the id of a robot
        """
    @typing.overload
    def is_id_robot(self, id: typing.SupportsFloat) -> bool:
        """
        tell if it's the id of a robot
        """
    def save_environment_screenshot(self, comment: str = '') -> None:
        """
        Save a screenshot of the actual environment at the current timestep in the logfolder.
        Parameters
        ----------
        
        comment: str
            string to append to the file name
        """
    def save_footprint_screenshot(self, comment: str = '') -> None:
        """
        Save a screenshot of the actual footprint at the current timestep in the logfolder.
        Parameters
        ----------
        
        comment: str
            string to append to the file name
        """
    def save_screenshot(self, comment: str = '') -> None:
        """
        Save a screenshot of the rendered frame in the logfolder.
        Parameters
        ----------
        
        comment: str
            string to append to the file name
        """
    def save_trajectory_image(self, comment: str = '') -> None:
        """
        Save a screenshot of the actual trajectory recorded at the current timestep in the logfolder.
        
        .. warning:
        
            Trajectory recording must be asked by calling pyroborobo.init_trajectory_monitor()
        
        Parameters
        ----------
        
        comment: str
            string to append to the file name
        """
    def start(self) -> None:
        """
        Starts the simulator.
        
        Starts the simulator, creates the window if the batch mode is not activated. Once started, it is impossible to
        modify the classes used to instantiate the different modules of the simulator or to change its configuration.
        """
    def update(self, nb_updates: typing.SupportsInt) -> bool:
        """
        Performs a simulator evaluation of ``nb_updates`` time steps.
        
        It is possible to call `update` multiple times. If the simulator is paused, then the frame generation has no impact
        on the number of updates.
        
        Parameters
        ----------
        self: pyroborobo.Pyroborobo
        nb_updates: int
            The number of simulator updates to do.
            If the simulator is paused, then the frame generation has no impact on the number of updates.
        
        Returns
        -------
        bool
            Has the end of the simulation been requested, either by roborobo itself or by closing the window
        
        Examples
        --------
        
        >>> roborobo.update(1000)  # run simulation for 1000 time steps
        >>> agents.learn()  # trigger agents' learning algorithms
        >>> roborobo.update(1000)  # Continue the simulation for 1000 more time steps
        """
    @property
    def agent_observers(self) -> PyObjectFastVector:
        """
        :class:`list` of :class:`~pyroborobo.AgentObserver`: The ordered list of all the agent observers in the simulation
        
        .. warning::
            :meth:`~pyroborobo.Pyroborobo.start` must have been called before using this property
        """
    @property
    def arena_size(self) -> tuple[int, int]:
        """
        Tuple[int, int]: The size of the arena
        """
    @property
    def controllers(self) -> PyObjectFastVector:
        """
        :class:`list` of :class:`~pyroborobo.Controller`: The ordered list of all the controllers in the simulation
        
        .. warning::
            :meth:`~pyroborobo.Pyroborobo.start` must have been called before using this property
        """
    @property
    def iterations(self) -> int:
        """
        The number of update iterations since the beginning of the simulation.
        """
    @property
    def landmarks(self) -> list[LandmarkObject]:
        """
        List[Landmark]: The list of all the landmarks in the environment
        """
    @property
    def objects(self) -> PyObjectFastVector:
        """
        :class:`list` of :class:`pyroborobo.PhysicalObject`: The ordered list of all the objects in the simulation.
        """
    @property
    def robot_index_offset(self) -> int:
        """
        int: Index at which the robot ids start
        
        Everything under this offset is a physical objects. Everything above is a robot.
        """
    @property
    def world_models(self) -> PyObjectFastVector:
        """
        :class:`list` of :class:`~pyroborobo.WorldModel`: The ordered list of all the world models in the simulation
        
        .. warning::
            :meth:`~pyroborobo.Pyroborobo.start` must have been called before using this property
        """
    @property
    def world_observer(self) -> typing.Any:
        """
        :obj:`pyroborobo.WorldObserver`: The World Observer of the roborobo environment
        
        .. warning::
            :meth:`~pyroborobo.Pyroborobo.start` must have been called before using this property
        """
class RoboroboSurface:
    def __buffer__(self, flags):
        """
        Return a buffer object that exposes the underlying memory of the object.
        """
    def __release_buffer__(self, buffer):
        """
        Release the buffer object that exposes the underlying memory of the object.
        """
class Robot:
    pass
class SquareObject(PhysicalObject):
    """
    
    SquareObject(id: int, data: dict) -> SquareObject
    
    Physical object with an axis-aligned rectangular shape
    
    Read :doc:`/tuto/objects` for a tutorial on how to use Objects.
    
    Parameters
    ----------
    id: int
        The id of the object
    data: dict (optional)
        The data for the object read from the properties file
    
    See also
    --------
    PhysicalObject: Reference for physical objects
    
    """
    @typing.overload
    def __init__(self, id: typing.SupportsInt = -1) -> None:
        ...
    @typing.overload
    def __init__(self, id: typing.SupportsInt = -1, data: dict = {}) -> None:
        ...
    def can_register(self) -> bool:
        """
        Can the object be registered at its current location
        
        Returns
        -------
        bool: Can the object be registered at its current location
        """
    def hide(self) -> None:
        """
        hide the object from the screen (collision can be still active)
        """
    def is_pushed(self, id: typing.SupportsInt, speed: tuple[typing.SupportsFloat, typing.SupportsFloat]) -> None:
        """
        Callback when the object is pushed
        
        Parameters
        ----------
        id: int
            The id of the robot that has pushed the object
        speed: tuple(double, double)
            The speed at which the robot pushed the object
        """
    def is_touched(self, id: typing.SupportsInt) -> None:
        """
        Callback when the object is touched
        
        Parameters
        ----------
        id: int
            The id of the robot that has touched the object
        """
    def is_walked(self, id: typing.SupportsInt) -> None:
        """
        Callback when the object is walked on
        
        Parameters
        ----------
        id: int
            The id of the robot that has walked on the object
        """
    def register(self) -> None:
        """
        Register the object (activate collision)
        """
    def set_color(self, red: typing.SupportsInt, blue: typing.SupportsInt, green: typing.SupportsInt) -> None:
        """
        set the (r,g,b) color for the object.
        Parameters
        ----------
        red: int
            The red component of the color in [0, 255]
        blue: int
            The blue component of the color in [0, 255]
        green: int
            The green component of the color in [0, 255]
        """
    def set_soft_height(self, height: typing.SupportsInt, force: bool = False) -> None:
        """
        Set the soft height (can be walked on) of the square object, if force is true, then no check is performed
        on registration.
        """
    def set_soft_width(self, width: typing.SupportsInt, force: bool = False) -> None:
        """
        Set the soft width (can be walked on) of the square object, if force is true, then no check is performed
        on registration.
        """
    def set_solid_height(self, height: typing.SupportsInt, force: bool = False) -> None:
        """
        Set the solid height of the square object, if force is true, then no check is performed
        on registration.
        """
    def set_solid_width(self, width: typing.SupportsInt, force: bool = False) -> None:
        """
        Set the solid width of the square object, if force is true, then no check is performed
        on registration.
        """
    def show(self) -> None:
        """
        show the object from the screen (collision can be still inactive)
        """
    def step(self) -> None:
        """
        Call at each timestep
        """
    def unregister(self) -> None:
        """
        Unregister the object (deactivate collision)
        """
    @property
    def id(self) -> int:
        """
        int: the id of the object
        """
    @property
    def soft_height(self) -> int:
        """
        int: the height (i.e. vertical length) of the soft part of the object (can be walked on) in pixel
        """
    @soft_height.setter
    def soft_height(self, arg1: typing.SupportsInt) -> None:
        ...
    @property
    def soft_width(self) -> int:
        """
        int: the width (i.e. horizontal length) of the soft part of the object (can be walked on) in pixel
        """
    @soft_width.setter
    def soft_width(self, arg1: typing.SupportsInt) -> None:
        ...
    @property
    def solid_height(self) -> int:
        """
        int: the height (i.e. vertical length) of the solid part of the object in pixel
        """
    @solid_height.setter
    def solid_height(self, arg1: typing.SupportsInt) -> None:
        ...
    @property
    def solid_width(self) -> int:
        """
        int: the width (i.e. horizontal length) of the solid part of the object in pixel
        """
    @solid_width.setter
    def solid_width(self, arg1: typing.SupportsInt) -> None:
        ...
class World:
    pass
class WorldModel:
    pass
class WorldObserver:
    def __init__(self, world: World) -> None:
        ...
    def init_post(self) -> None:
        """
        Called after initialising robots & objects.
        """
    def init_pre(self) -> None:
        """
        Called before initialising robots & objects.
        """
    def step_post(self) -> None:
        """
        Call at each time step after the steps of objects and robots
        """
    def step_pre(self) -> None:
        """
        Call at each time step before the steps of objects and robots
        """
