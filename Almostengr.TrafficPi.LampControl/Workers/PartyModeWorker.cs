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
        private readonly GpioController _gpio;

        public PartyModeWorker(ILogger<PartyModeWorker> logger, GpioController gpioController, AppSettings appSettings) :
            base(logger, appSettings)
        {
            _logger = logger;
            _gpio = gpioController;
        }

        public override Task StartAsync(CancellationToken cancellationToken)
        {
            InitializeGpio(_gpio);
            return base.StartAsync(cancellationToken);
        }

        public override Task StopAsync(CancellationToken cancellationToken)
        {
            ShutdownGpio(_gpio);
            return base.StopAsync(cancellationToken);
        }

        protected override async Task ExecuteAsync(CancellationToken stoppingToken)
        {
            while (!stoppingToken.IsCancellationRequested)
            {
                int phase = random.Next(1, 7);

                switch (phase)
                {
                    case 1:
                        ChangeSignal(LampOn, LampOff, LampOff, _gpio);
                        break;

                    case 2:
                        ChangeSignal(LampOff, LampOn, LampOff, _gpio);
                        break;

                    case 3:
                        ChangeSignal(LampOff, LampOff, LampOn, _gpio);
                        break;

                    case 4:
                        ChangeSignal(LampOn, LampOn, LampOff, _gpio);
                        break;

                    case 5:
                        ChangeSignal(LampOff, LampOn, LampOn, _gpio);
                        break;

                    case 6:
                        ChangeSignal(LampOn, LampOn, LampOn, _gpio);
                        break;
                    
                    case 7:
                        ChangeSignal(LampOn, LampOff, LampOn, _gpio);
                        break;

                    default:
                        ChangeSignal(LampOff, LampOff, LampOff, _gpio);
                        break;
                }

                await Task.Delay(TimeSpan.FromSeconds(1), stoppingToken);
            }
        }

    }
}