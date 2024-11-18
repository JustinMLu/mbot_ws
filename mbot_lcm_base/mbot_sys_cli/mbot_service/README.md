> This tool is to manage and monitor MBot system services.

## Usage

```
mbot service {list|status|log|start|stop|restart|enable|disable} [service_name]
```
```
Actions:
  list       List all mbot- services
  status     Status of all mbot- services or a specific service
  log        Show log for the service
  start      Start the service
  stop       Stop the service
  restart    Restart the service
  enable     Enable the service (not immediate start)
  disable    Disable the service (not immediate stop)

Examples:
  mbot service list
  mbot service status
  mbot service status mbot-xxx.service
  mbot service log mbot-xxx.service
  mbot service start mbot-xxx.service
  mbot service stop mbot-xxx.service
  mbot service restart mbot-xxx.service
  mbot service enable mbot-xxx.service
  mbot service disable mbot-xxx.service
```