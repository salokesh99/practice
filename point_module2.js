"use strict";
exports.__esModule = true;
var point_module1_1 = require("./point_module1");
var pointObject2 = new point_module1_1.PointedClass2(2, 4);
// we can change the value dynamically. if it is public. Else we can not.
// pointObject1.x = 11
// pointObject1.y = 12
pointObject2.draw();
// let x = pointObject1.getX()
// pointObject1.setX(10)
// let b1 =  pointObject2.X
// pointObject2.X = 10
