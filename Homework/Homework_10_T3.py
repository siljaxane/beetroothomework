class TV_contraoller:
    def __init__(self, first_channel, last_channel, turn_channel, next_channel, previous_channel, current_channel):
        self.first_channel = first_channel
        self.last_channel = last_channel
        self.turn_channel = turn_channel
        self.next_channel = next_channel
        self.previous_channel = previous_channel
        self.current_channel = current_channel

    def first_channel(first_channel):
        return controller.first_channel() == 'BBC'

    def last_channel(last_channel):
        return controller.last_channel() == 'TV1000'

    def turn_channel(turn_channel):
        return controller.turn_channel() == 'BBC'

    def next_channel(next_channel):
        return controller.next_channel() == 'Discovery'

    def previous_channel(previous_channel):
        return controller.previous_channel() == 'BBC'

    def current_channel(current_channel):
        return controller.current_channel() == "BBC"

def is_exist(N):
    if is_exist in CHANNELS == True:
        print('YES')
    else:
        print('NO')

controller = TV_contraoller(CHANNELS)

print(controller)