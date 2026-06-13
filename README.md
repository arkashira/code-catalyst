# Code Catalyst
A project for automatic scaling based on traffic.

## Usage
1. Create a `Deployment` object with a `ScalingConfig`.
2. Call the `scale` method to adjust the pod count based on CPU usage.
3. Use the `log_scaling_event` method to log scaling events.
4. Convert the `Deployment` object to a dictionary using the `to_dict` method.
