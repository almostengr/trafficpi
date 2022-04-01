using System;
using System.Threading;
using System.Threading.Tasks;
using Almostengr.TrafficPi.LampControl.Common;
using Almostengr.TrafficPi.LampControl.Services;
using Microsoft.Extensions.Logging;

namespace Almostengr.TrafficPi.LampControl.Workers
{
    public class UsTrafficWithSensorWorker : BaseWorker
    {
        private readonly ISensorService _carWaitingSensor;

        public UsTrafficWithSensorWorker(ILogger<BaseWorker> logger, ISignalIndicationService signalIndication,
            ISensorService carWaitingSensor) :
            base(logger, signalIndication)
        {
            _carWaitingSensor = carWaitingSensor;
        }

        protected override async Task ExecuteAsync(CancellationToken stoppingToken)
        {
            while (!stoppingToken.IsCancellationRequested)
            {
                _signalIndication.GreenLight();
                await Task.Delay(TimeSpan.FromSeconds(RedGreenDelay()), stoppingToken);

                _signalIndication.YellowLight();
                await Task.Delay(TimeSpan.FromSeconds(YellowDelay()), stoppingToken);

                _signalIndication.RedLight();
                await Task.Delay(TimeSpan.FromSeconds(10), stoppingToken);

                for(int i = 0; i < 180; i++)
                {
                    bool buttonPressed = _carWaitingSensor.IsButtonPressed(InputPin.CarSensor);
                    await Task.Delay(TimeSpan.FromSeconds(1), stoppingToken);

                    if (buttonPressed)
                    {
                        _logger.LogInformation($"Car is waiting");
                        await Task.Delay(TimeSpan.FromSeconds(YellowDelay() + 1), stoppingToken);
                        break;
                    }
                } // end for
            } // end while
        }

    }
}