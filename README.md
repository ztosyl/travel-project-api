### Travel Project API

This app is a travel planning app. A user is able to log on, post a plan to take a trip, and then click on that trip to add itinerary items. The client is hooked up to two third-party APIs, one which returns live flight data and one which returns live hotel data, and the user can use those to complete their plans when creating them. A quick note: as of now, the hotel data includes already booked hotels. This was done for testing/display purposes, because it is extremely difficult to find hotels on the database that aren't already booked (the queries often turned up empty.)

## Repo Links

[Client](https://github.com/ztosyl/travel-project-client)
[API](https://github.com/ztosyl/travel-project-api)

## Deployed Links

[Client](https://ztosyl.github.io/travel-project-client)
[API](https://travel-project-api.herokuapp.com)

### Technologies Used

For this API, I used Django and Python, CORS, and Heroku for deployment.

## Improvements

### Categorize Itineraries by Day
In a future version of this project, I'd like to be able to group itinerary items by day. They are currently in order by time, however not grouped beyond that, and I think it would make sense to have them clustered by what day they are on. This may even include an intermediate page or accordion where the user could click on a day and see what they had planned for that day.

### Amadeus Point of Interest API integration
In addition to the Flights and Hotels APIs, Amadeus also has a Point of Interest API, which I think could be interesting to integrate on the Itinerary side.

### Maps integration
I'd also like to integrate some kind of maps API, that could give a user directions from the airport to the hotel, or the hotel to a point of interest.

## Development/Problem Solving Process

In order to make my workflow go smoothly, I started this project by completely doing the backend before starting on the frontend client, so that the client was communicating with a functional API.

I started by making Plans, and deciding what should go in them. Since four flight times had to be indicated in separate keys, I struggled with naming them clearly. I think in the final product they still aren't totally clearly named, so I added comments to facilitate that. I then moved on to CRUD actions. For a Plan, the main resource of the project, one should be able to index, show, delete, post and update plans. I decided it would be best to write the index/get functions to only display plans owned by the current user, because in the context of the site itself, it wouldn't make sense for a user to see the plans of other users.

I did the same with Itineraries, decided what should go in them and tried to name them as appropriately as possible. However, with itineraries, you would only want to get itineraries associated with a certain plan, so I formulated my GET as such. All itinerary CRUD actions are associated with a plan.

## ERD

[ERD](https://media.git.generalassemb.ly/user/27606/files/03670080-b465-11ea-99c8-d013ac4daf5d)

## Routes

### Plans
| Request      | Route | Description |
| ----------- | ----------- | ----------- |
| GET      | /plans | Index all plans associated with the current user |
| POST   | /plans | Post one plan as the current user |
| GET   | plans/<int:pk>/ | Show one plan by PK |
| DELETE   | plans/<int:pk>/ | Delete one plan by PK |
| UPDATE   | plans/<int:pk>/ | Update one plan by PK |

### Itineraries
| Request      | Route | Description |
| ----------- | ----------- | ----------- |
| GET      | plans/<int:pk>/itineraries | Index all itineraries associated with a plan |
| POST   | plans/<int:pk>/itineraries | Post one iinerary to a specific plan |
| GET   | itineraries/<int:pk>/ | Show one itinerary by PK |
| DELETE   | itineraries/<int:pk>/ | Delete one itinerary by PK |
| UPDATE   | itineraries/<int:pk>/ | Update one itinerary by PK |

## Installation Instructions

To install this app, fork and git clone it to your local system. Then run pipenv shell in the terminal to start the virtual environment, and then pipenv install to install dependencies.
