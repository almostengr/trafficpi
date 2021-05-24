using System;
using System.Device.Gpio;
using System.Threading;
using System.Threading.Tasks;
using Microsoft.Extensions.Logging;

namespace Almostengr.TrafficPi.LampControl.Workers
{
    public class PartyModeWorker : BaseWorker
    {
        private readonly ILogger<PartyModeWorker> _logger;

        public PartyModeWorker(ILogger<PartyModeWorker> logger, GpioController gpioController, AppSettings appSettings) :
            base(logger, gpioController, appSettings)
        {
            _logger = logger;
        }

        protected override async Task ExecuteAsync(CancellationToken stoppingToken)
        {
            while (!stoppingToken.IsCancellationRequested)
            {
                int phase = random.Next(1, 7);

                switch (phase)
                {
                    case 1:
                        ChangeSignal(LampOn, LampOff, LampOff);
                        break;

                    case 2:
                        ChangeSignal(LampOff, LampOn, LampOff);
                        break;

                    case 3:
                        ChangeSignal(LampOff, LampOff, LampOn);
                        break;

                    case 4:
                        ChangeSignal(LampOn, LampOn, LampOff);
                        break;

                    case 5:
                        ChangeSignal(LampOff, LampOn, LampOn);
                        break;

                    case 6:
                        ChangeSignal(LampOn, LampOn, LampOn);
                        break;
                    
                    case 7:
                        ChangeSignal(LampOn, LampOff, LampOn);
                        break;

                    default:
                        ChangeSignal(LampOff, LampOff, LampOff);
                        break;
                }

                await Task.Delay(TimeSpan.FromSeconds(1), stoppingToken);
            }
        }
    }
}