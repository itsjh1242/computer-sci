var curry = function (method) {
  return function (a) {
    return function (b) {
      return function (c) {
        return method(a, b, c);
      };
    };
  };
};

var getMax = curry(Math.max);
console.log(getMax(10));
console.log(getMax(8));
console.log(getMax(145));

var curry2 = (method) => (a) => (b) => (c) => (d) => (e) => method(a, b, c, d, e);
var getMin = curry2(Math.min)(1)(2);
console.log(getMin(3)(4)(5));
