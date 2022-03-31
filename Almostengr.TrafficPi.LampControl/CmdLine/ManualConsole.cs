using System;
using Almostengr.TrafficPi.LampControl.Services;

namespace Almostengr.TrafficPi.LampControl.CmdLine
{
    public static class ManualConsole
    {
        public static void RunProgram()
        {
            ISignalIndicationService signalIndication = new SignalIndicationService();

            Console.CancelKeyPress += (s, e) =>
            {
                Console.WriteLine("Shutting down");
                signalIndication.ShutdownLights();
            };
            
            string input = string.Empty;
            while (input != "q")
            {
                Console.WriteLine("==== Main Menu ====");
                Console.WriteLine("0 - All Off, 1 - Red, 2 - Yellow, 3 - Green, 4 - All On, Q - Quit");
                Console.WriteLine();
                Console.WriteLine("Enter selection: ");

                input = Console.ReadLine().ToLower();

                switch (input)
                {
                    case "0":
                        signalIndication.NoLights();
                        break;

                    case "1":
                        signalIndication.RedLight();
                        break;

                    case "2":
                        signalIndication.YellowLight();
                        break;

                    case "3":
                        signalIndication.GreenLight();
                        break;
                        
                    case "4":
                        signalIndication.AllLights();
                        break;

                    case "q":
                        Console.WriteLine("Exiting");
                        signalIndication.ShutdownLights();
                        break;

                    default:
                        Console.WriteLine("Invalid selection");
                        break;
                }
            } // end while
        }

    }
}
