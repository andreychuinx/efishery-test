# efishery-test

## Installation
First, you need to clone this repository:
```bash
git clone git@github.com:andreychuinx/efishery-test.git
```

Then change into the `efishery-test` folder:
```bash
cd efishery-test
```
create .env
```bash
AUTH_PORT=3000
FETCH_PORT=3001
JWT_SECRET=test
API_KEY_CONVERTER={YOUR_API_KEY_CONVERTER}
```
you can take API KEY CONVERTER from freecurrencyapi.com
Then run docker-compose
```bash
docker-compose up
```

## Diagram
```
                                                  
           +----------------+                      
           |   API Gateway  |                      
           +----------------+                             
                     |                            
           +----------------+    +----------------+
           |  Authentication|    |   auth-api      |
           |      Server    |    |                 |
           +----------------+    +----------------+
                     |                            
           +----------------+    +----------------+                  
           |    Services    |    |    fetch-api   |                  
           +----------------+    +----------------+                  
                     |                            
           +----------------+    +----------------+                   
           |     Data       |    |   json file    |                  
           |    Storage     |    +----------------+                  
           +----------------+                      
```                                      
## API AVAILABLES
you can download insomnia collection on this repo
