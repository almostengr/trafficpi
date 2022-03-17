using Microsoft.Extensions.Logging;

namespace Almostengr.TrafficPi.LampControl.Services
{
    public class MockSignalIndicationService : ISignalIndicationService
    {
        private readonly ILogger<MockSignalIndicationService> _logger;

        public MockSignalIndicationService(ILogger<MockSignalIndicationService> logger)
        {
            _logger = logger;
        }

        public void AllLights()
        {
            _logger.LogInformation("All lights");
        }

        public void GreenLight()
        {
            _logger.LogInformation("Green light");
        }

        public void InitializeLights()
        {
            _logger.LogInformation("Initializing lights");
        }

        public void NoLights()
        {
            _logger.LogInformation("No lights");
        }

        public void RedGreenLights()
        {
            _logger.LogInformation("Red and green lights");
        }

        public void RedLight()
        {
            _logger.LogInformation("Red light");
        }

        public void RedYellowLights()
        {
            _logger.LogInformation("Red and yellow lights");
        }

        public void ShutdownLights()
        {
            _logger.LogInformation("Shutting down lights");
        }

        public void YellowGreenLights()
        {
            _logger.LogInformation("Yellow and green lights");
        }

        public void YellowLight()
        {
            _logger.LogInformation("Yellow light");
        }
    }
}
