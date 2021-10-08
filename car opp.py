class Car():
    max_speed = 160
    consumption_per_100km = 1.5
    colour = "white"
    status = 'off'
    speed = 0
    
    def start(self):
        self.status = 'on'
        self.speed += 5
    
    def accelerate(self):
        self.speed += 10
    
    def stop(self):
        self.speed = 0
        self.status = 'off'
        
    def speedometer(self):
        print(f'The car is running at {self.speed} km/h')
        
    def report(self):
        movement = ''
        if self.status == 'off': movement = 'stopped'
        elif self.status == 'on': movement = 'running'
        print(f'The car is {movement}.')
        if self.status == 'on' :
            print(f'The car is currently running at {self.speed} km/h.')
ibiza = Car()
print('I start the engine...')
ibiza.start()
for i in range(5):
    ibiza.speedometer()
    ibiza.accelerate()
ibiza.report()
ibiza.stop()
ibiza.report()