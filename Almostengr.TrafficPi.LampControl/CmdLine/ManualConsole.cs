using System;
using System.Device.Gpio;

namespace Almostengr.TrafficPi.LampControl.CmdLine
{
    public static class ManualConsole
    {
        public static void RunProgram()
        {
            PinValue LampOff = PinValue.High;
            PinValue LampOn = PinValue.Low;
            using GpioController gpioController = new GpioController();
            string input = string.Empty;

            gpioController.OpenPin(11, PinMode.Output);
            gpioController.OpenPin(9, PinMode.Output);
            gpioController.OpenPin(10, PinMode.Output);

            Console.CancelKeyPress += (s, e) =>
            {
                Console.WriteLine("Shutting down");
                ChangeSignal(LampOff, LampOff, LampOff, gpioController);
            };

            while (input.ToLower() != "q")
            {
                Console.WriteLine("==== Main Menu ====");
                Console.WriteLine();
                Console.WriteLine("0 - All Off, 1 - Red, 2 - Yellow, 3 - Green, Q - Quit");
                Console.WriteLine();

                input = Console.ReadLine();

                switch (input)
                {
                    case "0":
                        ChangeSignal(LampOff, LampOff, LampOff, gpioController);
                        break;

                    case "1":
                        ChangeSignal(LampOn, LampOff, LampOff, gpioController);
                        break;

                    case "2":
                        ChangeSignal(LampOff, LampOn, LampOff, gpioController);
                        break;

                    case "3":
                        ChangeSignal(LampOff, LampOff, LampOn, gpioController);
                        break;

                    case "q":
                    case "Q":
                        Console.WriteLine("Exiting");
                        break;

                    default:
                        Console.WriteLine("Invalid selection");
                        break;
                }
            } // end while

            gpioController.ClosePin(11);
            gpioController.ClosePin(9);
            gpioController.ClosePin(10);
        }

        public static void ChangeSignal(PinValue redLight, PinValue yellowLight, PinValue greenLight, GpioController gpioController)
        {
            gpioController.Write(11, redLight);
            gpioController.Write(9, yellowLight);
            gpioController.Write(10, greenLight);
        }

    }
}