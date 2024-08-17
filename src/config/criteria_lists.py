angular_criteria_list = [
    "Dependency Injection: Assess the use of Angular's dependency injection system. Consider the use of @Injectable decorators, constructor injection, and providers. Look for correct and efficient implementation.",
    "Lazy Loading for Modules/Routes: Evaluate the implementation of lazy loading for Angular modules and routes. Check for the use of loadChildren in route definitions and efficient module loading practices.",
    "Routing Setup: Examine the configuration of the Angular Router. Consider the setup of RouterModule, Routes, and the use of <router-outlet>. Evaluate navigation logic and route guards if present.",
    "Angular Forms: Analyze the implementation of Angular forms, both template-driven and reactive. Check the use of FormGroup, FormControl, FormBuilder, ngModel, form validation, and handling of form value changes.",
    "RXJS Usage: Review the usage of RXJS for handling asynchronous operations. Look for effective use of observables, operators (e.g., map, mergeMap, switchMap), and proper subscription/unsubscription practices.",
    "Component Design: Evaluate the design and structure of Angular components. Consider the use of standalone components, shared components, and reusable patterns. Look for modularity, maintainability, and adherence to Angular best practices.",
    "Styling and Angular Material/CDK: Assess the implementation of styles using Angular Material components and Angular CDK for drag-and-drop functionality. Check for consistent styling practices and proper use of Angular Material APIs.",
]

python_criteria_list = [
    "Code Style and Quality: Evaluate the adherence to PEP 8 standards, readability of the code, and use of docstrings for documentation. Check for consistent naming conventions and code layout.",
    "Use of Libraries and Frameworks: Assess the appropriateness and efficiency of imported libraries and frameworks. Consider whether the choices, such as Flask, Django, or NumPy, suit the project's requirements.",
    "Exception Handling: Review the implementation of error handling strategies. Look for the use of try-except blocks, the raising of custom exceptions, and ensuring that exceptions are specific and helpful.",
    "Function Design: Analyze the modularity and design of functions. Check for clear, concise, and single-responsibility functions. Evaluate the use of parameters, return values, and their type hints.",
    "Object-Oriented Practices: Examine the use of classes and object-oriented programming principles such as encapsulation, inheritance, and polymorphism. Assess the use of class methods, static methods, and properties.",
    "Testing and Testability: Evaluate the presence and quality of unit tests using frameworks like unittest or pytest. Look for good coverage, use of mocks and fixtures, and whether tests are comprehensive and meaningful.",
    "Performance Optimization: Review the code for performance efficiency. Check for the use of appropriate data structures, algorithmic efficiency, and potential improvements using profiling tools.",
    "Security Practices: Assess the implementation of security best practices, such as input validation, secure handling of credentials, and protection against common vulnerabilities like SQL injections or cross-site scripting in web applications.",
    "Concurrency and Parallelism: Review the use of concurrency modules like asyncio, threading, or multiprocessing. Evaluate the correct and effective use of these paradigms to handle asynchronous tasks or parallel processing.",
    "Packaging and Deployment: Examine the setup for package management and deployment configurations. Look for the use of requirements.txt, setup.py, or containerization with Docker. Evaluate the clarity and reliability of build and deployment scripts."
]

flutter_criteria_list = [
    "State Management: Evaluate the state management approach used in the Flutter project. Look for the use of providers, blocs, Redux, or other state management techniques. Assess how state is passed between widgets and the overall efficiency of state updates.",
    "Widget Composition and Reusability: Examine the composition and reusability of widgets within the project. Assess the use of stateless and stateful widgets, custom widgets, and the extent of modularization to promote reuse and maintainability.",
    "Navigation and Routing: Review the implementation of navigation and routing. Consider the setup of the Navigator and named routes, and assess the use of context for navigating between screens. Check for the presence of deep linking capabilities.",
    "API Integration and Network Handling: Analyze how the application communicates with external services. Evaluate the use of packages like http or dio for making network requests, handling of asynchronous operations, and error handling in network communications.",
    "UI and UX Practices: Assess the consistency and responsiveness of the UI. Check for the effective use of themes, animations, and transitions. Evaluate accessibility features and adherence to material design or Cupertino design principles.",
    "Performance Optimization: Review performance aspects of the Flutter app. Check for efficient list rendering with ListView.builder, use of const widgets, and profiling for performance issues using the Flutter performance tools.",
    "Testing Strategies: Evaluate the testing strategy including unit tests, widget tests, and integration tests. Look for the use of the Flutter Test Framework and Mockito for testing dependencies. Assess test coverage and the effectiveness of tests.",
    "Error Handling and Debugging: Examine practices for error handling and debugging. Assess the implementation of try-catch blocks, use of assertions, and how the app handles potential crashes or errors.",
    "Code Organization and Architecture: Review the project's code organization and architectural approach. Consider the use of MVC, MVVM, or Clean Architecture patterns. Evaluate the separation of concerns and scalability of the codebase.",
    "Package Management and Dependency Control: Check for the management of dependencies via pubspec.yaml. Evaluate the choice and versions of third-party packages, and consider potential issues with package compatibility or outdated dependencies."
]

