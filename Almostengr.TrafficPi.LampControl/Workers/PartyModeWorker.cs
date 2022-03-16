using System;
using System.Device.Gpio;
using System.Threading;
using System.Threading.Tasks;
using Almostengr.TrafficPi.LampControl.Services;
using Microsoft.Extensions.Logging;

namespace Almostengr.TrafficPi.LampControl.Workers
{
    public class PartyModeWorker : BaseWorker
    {
        public PartyModeWorker(ILogger<BaseWorker> logger, ISignalIndicationService signalIndication) : base(logger, signalIndication)
        {
        }


        // private readonly GpioController _gpio;

        // public PartyModeWorker(ILogger<FlashGreenWorker> logger, GpioController gpio) : 
        //     base(logger)
        // {
        //     _gpio = gpio;
        // }

        // public override Task StartAsync(CancellationToken cancellationToken)
        // {
        //     InitializeGpio(_gpio);
        //     return base.StartAsync(cancellationToken);
        // }

        // public override Task StopAsync(CancellationToken cancellationToken)
        // {
        //     ShutdownGpio(_gpio);
        //     return base.StopAsync(cancellationToken);
        // }

        protected override async Task ExecuteAsync(CancellationToken stoppingToken)
        {
            while (!stoppingToken.IsCancellationRequested)
            {
                int phase = random.Next(1, 7);

                switch (phase)
                {
                    case 1:
                        // ChangeSignal(LampOn, LampOff, LampOff, _gpio);
                        _signalIndication.RedLight();
                        break;

                    case 2:
                        // ChangeSignal(LampOff, LampOn, LampOff, _gpio);
                        _signalIndication.YellowLight();
                        break;

                    case 3:
                        // ChangeSignal(LampOff, LampOff, LampOn, _gpio);
                        _signalIndication.GreenLight();
                        break;

                    case 4:
                        // ChangeSignal(LampOn, LampOn, LampOff, _gpio);
                        _signalIndication.RedYellowLights();
                        break;

                    case 5:
                        // ChangeSignal(LampOff, LampOn, LampOn, _gpio);
                        _signalIndication.YellowGreenLights();
                        break;

                    case 6:
                        // ChangeSignal(LampOn, LampOn, LampOn, _gpio);
                        _signalIndication.AllLights();
                        break;
                    
                    case 7:
                        // ChangeSignal(LampOn, LampOff, LampOn, _gpio);
                        _signalIndication.RedGreenLights();
                        break;

                    default:
                        // ChangeSignal(LampOff, LampOff, LampOff, _gpio);
                        _signalIndication.NoLights();
                        break;
                }

                await Task.Delay(TimeSpan.FromSeconds(1), stoppingToken);
            }
        }

    }
}