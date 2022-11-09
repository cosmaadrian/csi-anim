

class Animator:
    def __init__(self):
        self.timesteps = []
        self.attributes = []
        self.do_repeat = False

    def at(self, timestep, attributes):
        self.timesteps.append(timestep)
        self.attributes.append(attributes)

    def apply_to(self, shape):
        return AnimatedShape(
            original = shape,
            timesteps = self.timesteps,
            attributes = self.attributes,
            repeat = self.do_repeat
        )

    def repeat(self):
        self.do_repeat = True


class AnimatedShape:
    def __init__(self, original, timesteps, attributes, repeat = False):
        self.original = original
        self.timesteps = timesteps
        self.attributes = attributes
        self.repeat = repeat
        self._step = 0

    def step(self):
        self._step += 1
        # get where you are
        previous_step_idx = -1

        for i in range(len(self.timesteps) - 1):
            if self._step < self.timesteps[i + 1] and self._step >= self.timesteps[i]:
                previous_step_idx = i
                break

        if previous_step_idx == -1:
            if self.repeat:
                self._step = 0
            return

        previous_attributes = self.attributes[previous_step_idx]
        next_attributes = self.attributes[previous_step_idx + 1]

        x = self._step % self.timesteps[previous_step_idx] if self.timesteps[previous_step_idx] else self._step
        percentage = (x) / (self.timesteps[previous_step_idx + 1] - self.timesteps[previous_step_idx])

        new_attributes = dict()
        for key in previous_attributes.keys():
            new_attributes[key] = int(previous_attributes[key] * (1 - percentage) + next_attributes[key] * (percentage))

        for key in new_attributes.keys():
            self.original.set(key, new_attributes[key])

    def draw(self, frame):
        return self.original.draw(frame)
