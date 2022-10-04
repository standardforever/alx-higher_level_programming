#!/usr/bin/node
exports.esrever = function (list) {
  let count = list.length;
  let hold;
  const num = count;
  for (let i = 0; i < num / 2; i++) {
    hold = list[i];
    list[i] = list[count - 1];
    list[count - 1] = hold;
    count--;
  }
  return (list);
};
