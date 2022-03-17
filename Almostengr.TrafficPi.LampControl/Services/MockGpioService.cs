namespace Almostengr.TrafficPi.LampControl.Services
{
    public class MockGpioService : IGpioService
    {
        public void CloseOutputPin(int pinNumber)
        {
            throw new System.NotImplementedException();
        }

        public void CloseOutputPins(int[] pinNumbers)
        {
            throw new System.NotImplementedException();
        }

        public void OpenOutputPin(int pinNumber)
        {
            throw new System.NotImplementedException();
        }

        public void OpenOutputPins(int[] pinNumbers)
        {
            throw new System.NotImplementedException();
        }

        public void TurnOffGpio(int pinNumber)
        {
            throw new System.NotImplementedException();
        }

        public void TurnOffGpio(int[] pinNumbers)
        {
            throw new System.NotImplementedException();
        }

        public void TurnOnGpio(int pinNumber)
        {
            throw new System.NotImplementedException();
        }

        public void TurnOnGpio(int[] pinNumbers)
        {
            throw new System.NotImplementedException();
        }
    }
}