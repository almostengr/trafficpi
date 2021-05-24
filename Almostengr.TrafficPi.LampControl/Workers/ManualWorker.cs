using System;
using System.Device.Gpio;
using System.Threading;
using System.Threading.Tasks;
using Microsoft.Extensions.Logging;

namespace Almostengr.TrafficPi.LampControl.Workers
{
    public class ManualWorker : BaseWorker
    {
        private readonly ILogger<ManualWorker> _logger;

        public ManualWorker(
            ILogger<ManualWorker> logger,
            GpioController gpioController,
            AppSettings appSettings) :
            base(logger, gpioController, appSettings)
        {
            _logger = logger;
        }

        protected override async Task ExecuteAsync(CancellationToken stoppingToken)
        {
            string input = string.Empty;

            while (input.ToLower() != "q" || !stoppingToken.IsCancellationRequested)
            {
                Console.WriteLine("==== Main Menu ====");
                Console.WriteLine();
                Console.WriteLine("0 - All Off, 1 - Red, 2 - Yellow, 3 - Green, Q - Quit");
                Console.WriteLine();

                input = Console.ReadLine().ToLower();

                switch (input)
                {
                    case "0":
                        ChangeSignal(LampOff, LampOff, LampOff);
                        break;

                    case "1":
                        ChangeSignal(LampOn, LampOff, LampOff);
                        break;

                    case "2":
                        ChangeSignal(LampOff, LampOn, LampOff);
                        break;

                    case "3":
                        ChangeSignal(LampOff, LampOff, LampOn);
                        break;

                    case "q":
                        _logger.LogInformation("Exiting...");
                        break;

                    default:
                        Console.WriteLine("Invalid selection");
                        break;
                }
                
                await Task.Delay(TimeSpan.FromMilliseconds(1), stoppingToken);
            } // end while
        }
    }
}