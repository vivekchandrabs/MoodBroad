# MoodBroad

# api.speckbit

## Getting Started with the Project

To get started with the project:
    
     $ git clone https://gitlab.com/speckbit/api.speckbit.com.git

To install all dependencies, create a new virutalenv with your preferred plugin and do:

      $ pip install -r requirements.txt
      
To run the project, Go to the root folder and run
 
      $ python manage.py runserver
 
## Api end point documentation:

### Authentication urls
 
| Api end-point  | Method| Function  | Argument | Description   | Response |
| ---------------| ------|-----------| ---------| --------------| ---------|
| /auth/register/| GET   | UserRegisteration() | "email" | Sends a verification email | json with a message and email |
| /auth/register/| POST | UserRegistration() | "email", "login_code" | Creates a new User | json with a token and user id |
| /auth/register/ | PUT | UserRegisteration() | "state", "email" | Creates a new User | json with a token and user id |
| /auth/login/ | GET | LoginView() | "email" | Sends a email with Login code and Magic Link | json with a message |
| /auth/login/  | POST | LoginView() |"email"| "login_code", "password" | Authenticates the user | json with a token,user id, token expiry time|
| /auth/logout/ | GET | LogoutView() | None | Logout the user | None |
| /auth/logoutall/ | GET | LogoutAllView() | None | Logout all the user | None |

### Profile urls:

| Api end-point  | Method| Function  | Argument | Description   | Response |
| ---------------| ------|-----------| ---------| --------------| ---------|
| /auth/profile/ | POST | ProfileViewSet() | organization, bio, , place, avatar, place |Creates the user profile | json with the user profile data |
| /auth/profile/ | GET | ProfileViewSet() | None | Returns the user profile | json with the user profile data | 
| /auth/toggle/star/ | POST | ToggleStarViewSet() | slug | Updates the roadmap star count, adds the user profile id to the roadmap and adds the roadmap id to the user profile | json with a message |

### Roadmap urls:

| Api end-point  | Method| Function  | Argument | Description   | Response |
| ---------------| ------|-----------| ---------| --------------| ---------|
| /roadmap/ | GET | RoadmapViewSet() | slug | Returns the particular roadmap | json with the roadmap attributes| 
| /roadmap/?filter="featured"  | GET | RoadmapViewSet() | None | Returns the Featured Roadmaps | json with the roadmap attributes| 
| /roadmap/?filter="popular" | GET | RoadmapViewSet() | None | Returns the Popular roadmap | json with the roadmap attributes| 
| /roadmap/?filter="similar" | GET | RoadmapViewSet() | None | Returns the Similar roadmap | json with the roadmap attributes| 
| /roadmap/?filter="all" | GET | RoadmapViewSet() | None | Returns the all roadmap | json with the roadmap attributes|
| /roadmap/?filter="verified" | GET | RoadmapViewSet() | None | Returns the verified roadmap | json with the roadmap attributes|
| /roadmap/register/ | GET | RoadmapSubscriptionViewSet() | None | Returns user roadmap subscriptions | json with the roadmap subscrption attributes| 
| /roadmap/register/ | POST | RoadmapSubscriptionViewSet() | slug | Create the user roadmap Subscription  | json with the roadmap subscription attributes | 
| /roadmap/milestones/ | GET | MilestoneViewSet() | slug  | Returns the milestones related to the roadmap | json with the milestones and actions of the particular attribute |
| /roadmap/category/ | GET | CategoryViewSet() | None | Returns the categories | json with the categories |

