using System;
using System.Device.Gpio;
using Almostengr.TrafficPi.LampControl.CmdLine;
using Almostengr.TrafficPi.LampControl.Services;
using Almostengr.TrafficPi.LampControl.Workers;
using Microsoft.Extensions.DependencyInjection;
using Microsoft.Extensions.Hosting;

namespace Almostengr.TrafficPi.LampControl
{
    public class Program
    {
        public static void Main(string[] args)
        {
            if (args.Length == 0 || args.Length >= 2)
            {
                ShowHelp();
            }
            else if (args[0] == "--manual")
            {
                ManualConsole.RunProgram();
            }
            else
            {
                CreateHostBuilder(args).Build().Run();
            }
        }

        public static IHostBuilder CreateHostBuilder(string[] args) =>
            Host.CreateDefaultBuilder(args)
                .ConfigureServices((hostContext, services) =>
                {
                    services.AddSingleton<GpioController>();

                    services.AddSingleton<IGpioService, GpioService>();
                    services.AddSingleton<ISignalIndicationService, SignalIndicationService>();

                    switch (args[0])
                    {
                        case "--mock":
                            services.AddHostedService<MockWorker>();
                            break;

                        case "--mock2":
                            services.AddHostedService<MockWorker2>();
                            break;

                        case "--us":
                            services.AddHostedService<UsTrafficWorker>();
                            break;

                        case "--uk":
                            services.AddHostedService<UkTrafficWorker>();
                            break;

                        case "--rglight":
                            services.AddHostedService<RedLightGreenLightWorker>();
                            break;

                        case "--rglightyellow":
                            services.AddHostedService<RedLightGreenLightWithYellowWorker>();
                            break;

                        case "--flashred":
                            services.AddHostedService<FlashRedWorker>();
                            break;

                        case "--flashyellow":
                            services.AddHostedService<FlashYellowWorker>();
                            break;

                        case "--flashgreen":
                            services.AddHostedService<FlashGreenWorker>();
                            break;

                        case "--solidred":
                            services.AddHostedService<RedLightWorker>();
                            break;

                        case "--solidyellow":
                            services.AddHostedService<YellowLightWorker>();
                            break;

                        case "--solidgreen":
                            services.AddHostedService<GreenLightWorker>();
                            break;
                        
                        case "--alllights":
                            services.AddHostedService<AllLightsWorker>();
                            break;

                        case "--partymode":
                            services.AddHostedService<PartyModeWorker>();
                            break;

                        default:
                            ShowHelp();
                            break;
                    }
                });

        public static void ShowHelp()
        {
            Console.WriteLine("===== PROGRAM HELP =====");
            Console.WriteLine();
            Console.WriteLine("--us - Run the signal using the US signal pattern");
            Console.WriteLine("--uk - Run the signal using the UK signal panttern");
            Console.WriteLine("--manual - Manually control each light");
            Console.WriteLine("--rglight - Run red light, green light");
            Console.WriteLine("--rglightyellow - Run red light, green light with yellow");
            Console.WriteLine("--flashred - Flash red signal");
            Console.WriteLine("--flashyellow - Flash yellow signal");
            Console.WriteLine("--flashgreen - Flash green signal");
            Console.WriteLine("--partymode - Randomly flash a signal color(s)");
            Console.WriteLine("--solidred - Solid red signal");
            Console.WriteLine("--solidyellow - Solid yellow signal");
            Console.WriteLine("--solidgreen - Solid green signal");
            Console.WriteLine("--alllights - All lights on solid");
        }

    }
}
