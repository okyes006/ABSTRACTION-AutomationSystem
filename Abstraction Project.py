from abc import ABC, abstractmethod
class BuildingSystem(ABC):
    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass

    @abstractmethod
    def status(self):
        pass

class AirConditioningSystem(BuildingSystem):
    def start(self):
        print('Air Conditioning: Has been turned on')
    def stop(self):
        print('Air Conditioning: Has been turned off')
    def status(self):
        print('Air Conditioning: Is working properly')

class LightingSystem(BuildingSystem):
    def start(self):
        print('Lighting: Has been turned on')
    def stop(self):
        print('Lighting: Has been turned off')
    def status(self):
        print('Lighting: Is working properly')

class SecuritySystem(BuildingSystem):
    def start(self):
        print('Security: Has been turned on')
    def stop(self):
        print('Security: Has been turned off')
    def status(self):
        print('Security: Is working properly')


class FireAlarmSystem(BuildingSystem):
    def start(self):
        print('Fire Alarm: Has been turned on')
    def stop(self):
        print('Fire Alarm: Has been turned off')
    def status(self):
        print('Fire Alarm: Is working properly')


def run_building_systems():
    systems = [
        AirConditioningSystem(),
        LightingSystem(),
        SecuritySystem(),
        FireAlarmSystem(),
    ]
    for system in systems:
        system.start()
        system.status()
        system.stop()
        print('-' * 30)


if __name__ == '__main__':
    run_building_systems()