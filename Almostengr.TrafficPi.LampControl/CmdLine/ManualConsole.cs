using System;
using System.Device.Gpio;
using Almostengr.TrafficPi.LampControl.Services;

namespace Almostengr.TrafficPi.LampControl.CmdLine
{
    public static class ManualConsole
    {
        public static void RunProgram()
        {
            // PinValue LampOff = PinValue.High;
            // PinValue LampOn = PinValue.Low;
            // using GpioController gpioController = new GpioController();
            string input = string.Empty;

            // gpioController.OpenPin(11, PinMode.Output);
            // gpioController.OpenPin(9, PinMode.Output);
            // gpioController.OpenPin(10, PinMode.Output);

            ISignalIndicationService signalIndication = new SignalIndicationService();

            Console.CancelKeyPress += (s, e) =>
            {
                Console.WriteLine("Shutting down");
                // ChangeSignal(LampOff, LampOff, LampOff, gpioController);
                // ClosePins(gpioController);
                signalIndication.ShutdownLights();
            };

            while (input != "q")
            {
                Console.WriteLine("==== Main Menu ====");
                Console.WriteLine("0 - All Off, 1 - Red, 2 - Yellow, 3 - Green, Q - Quit");
                Console.WriteLine();
                Console.WriteLine("Enter selection: ");

                input = Console.ReadLine().ToLower();

                switch (input)
                {
                    case "0":
                        // ChangeSignal(LampOff, LampOff, LampOff, gpioController);
                        signalIndication.NoLights();
                        break;

                    case "1":
                        // ChangeSignal(LampOn, LampOff, LampOff, gpioController);
                        signalIndication.RedLight();
                        break;

                    case "2":
                        // ChangeSignal(LampOff, LampOn, LampOff, gpioController);
                        signalIndication.YellowLight();
                        break;

                    case "3":
                        // ChangeSignal(LampOff, LampOff, LampOn, gpioController);
                        signalIndication.GreenLight();
                        break;

                    case "q":
                        Console.WriteLine("Exiting");
                        break;

                    default:
                        Console.WriteLine("Invalid selection");
                        break;
                }
            } // end while
            
            // ClosePins(gpioController);
            signalIndication.ShutdownLights();
        }

        // private static void ClosePins(GpioController gpioController)
        // {
        //     gpioController.ClosePin(11);
        //     gpioController.ClosePin(9);
        //     gpioController.ClosePin(10);
        // }

        // private static void ChangeSignal(PinValue redLight, PinValue yellowLight, PinValue greenLight, GpioController gpioController)
        // {
        //     gpioController.Write(11, redLight);
        //     gpioController.Write(9, yellowLight);
        //     gpioController.Write(10, greenLight);
        // }

    }
}