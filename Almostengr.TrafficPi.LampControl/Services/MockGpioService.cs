using Microsoft.Extensions.Logging;

namespace Almostengr.TrafficPi.LampControl.Services
{
    public class MockGpioService : IGpioService
    {
        private readonly ILogger<MockGpioService> _logger;

        public MockGpioService(ILogger<MockGpioService> logger)
        {
            _logger = logger;
        }

        public void CloseOutputPin(int pinNumber)
        {
            _logger.LogInformation($"Closing output pin {pinNumber}");
        }

        public void CloseOutputPins(int[] pinNumbers)
        {
            foreach(var pinNumber in pinNumbers)
            {
                CloseOutputPin(pinNumber);
            }
        }

        public void OpenOutputPin(int pinNumber)
        {
            _logger.LogInformation($"Opening output pin {pinNumber}");
        }

        public void OpenOutputPins(int[] pinNumbers)
        {
            foreach(var pinNumber in pinNumbers)
            {
                OpenOutputPin(pinNumber);
            }
        }

        public void TurnOffGpio(int pinNumber)
        {
            _logger.LogInformation($"Turning off gpio pin {pinNumber}");
        }

        public void TurnOffGpio(int[] pinNumbers)
        {
            foreach(var pinNumber in pinNumbers)
            {
                TurnOffGpio(pinNumber);
            }
        }

        public void TurnOnGpio(int pinNumber)
        {
            _logger.LogInformation($"Turning on gpio pin {pinNumber}");
        }

        public void TurnOnGpio(int[] pinNumbers)
        {
            foreach(var pinNumber in pinNumbers)
            {
                TurnOnGpio(pinNumber);
            }
        }
    }
}