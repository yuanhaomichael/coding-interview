const EventEmitter = require('events');

class MyEmitter extends EventEmitter {
  constructor() {
    super(); // Calling the parent constructor
  }
}

const emitter1 = new MyEmitter();
emitter1.on('event1', () => {
  console.log('Event 1 triggered');
});

emitter1.emit('event1');

const emitter2 = new EventEmitter();

// Listener for event2
emitter2.on('event2', () => {
  console.log('Event 2 triggered');
});

//  event is emitted in the next tick of the Node.js event loop.
process.nextTick(() => {
  emitter2.emit('event2');
});


const emitter3 = new EventEmitter();

// Listener for event3
emitter3.on('event3', () => {
  console.log('Event 3 triggered');
});

//  emitted after I/O events of the current event loop cycle.
setImmediate(() => {
  emitter3.emit('event3');
});