
In scaling VogueX, our fashion recommender system, we aimed to build a highly adaptable, responsive system that efficiently handles fluctuating user demands while ensuring optimal performance and availability.

### Initial Scaling with Cloud Architecture

For initial scalability, we deployed VogueX on an AWS EC2 instance with auto-scaling enabled, which allows for vertical scaling as demand increases, supporting up to 1,000 users at once. However, this approach has some limitations:
- **Single Point of Failure**: Relying on one instance means any server failure would bring the entire application down.
- **High Costs**: Vertical scaling can be cost-intensive as increasing capacity requires more powerful resources.
- **Limited Vertical Scaling**: EC2 instances have an upper limit for scaling, restricting potential growth.

### Transition to Serverless Framework with AWS Lambda

To overcome these limitations, we deployed VogueX using AWS Lambda with Zappa, taking advantage of our free-tier credits. Lambda’s serverless architecture enables dynamic scaling, supporting up to 1,000 user requests per second and reducing our dependency on a single instance. However, our weather-based recommendations rely on an external API, and delays in the API response can cause interruptions in Lambda functions due to execution time limits.

### Proposed Microservices Architecture with Independent Modules

To further improve scalability and performance, we designed a modular, microservices-based architecture. Though we couldn’t fully implement it, we thoroughly evaluated the architecture, aiming to separate our application’s features into independent, serverless modules:

1. **Authentication**  
   - As authentication occurs once per session, this module can operate independently and be deployed serverlessly, reducing unnecessary resource usage. We generate an authentication token, which is stored in the client’s browser cache and sent with each request to the backend.

2. **Recommendations & Weather Forecast**  
   - These modules are closely integrated to provide weather-specific outfit suggestions. As recommendations are dependent on weather data, both modules are housed in a single service to minimize API call redundancy. User preferences are cached locally in the browser for faster responses and reduced backend requests.

3. **Favorites**  
   - The Favorites module operates independently, interfacing directly with client data without requiring constant availability. This is suitable for a serverless deployment, running only when a user accesses or modifies their favorite items.

4. **Virtual Try-On**  
   - The Virtual Try-On feature is a core component of VogueX, allowing users to preview outfits in AR. Given its high processing demands, we are considering using AWS Elastic Container Service (ECS) to host the AR models and provide scalable infrastructure for this feature. By deploying this in a containerized environment, we ensure it can scale horizontally to accommodate increased demand without affecting other services.

5. **Database**  
   - To address database scaling, which often becomes a bottleneck, we’re currently using MySQL but plan to migrate to SQLite, a serverless database. This migration will eliminate server dependency, enhancing overall scalability and reducing costs.

The microservices-based architecture thus divides VogueX into decoupled, independently scalable modules, each tailored for optimal performance and resource efficiency. 

### Architecture Summary

Our final architecture distributes VogueX functionalities across distinct services, each built to handle its unique demands. By adopting a serverless and containerized approach, we achieve a highly scalable, resilient system prepared to accommodate the growth of VogueX's user base and features. 
