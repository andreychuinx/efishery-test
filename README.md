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