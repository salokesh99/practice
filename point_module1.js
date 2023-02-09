"use strict";
exports.__esModule = true;
exports.PointedClass2 = void 0;
var PointedClass2 = /** @class */ (function () {
    // private x: number ;
    // private y:number ;
    // optional constructors need a question mark after the decalaration
    function PointedClass2(x, y) {
        this.x = x;
        this.y = y;
    }
    // constructor(x: number, y:number){
    //     this.x = x;
    //     this.y = y;
    // }
    PointedClass2.prototype.draw = function () {
        console.log('drawing x and y', this.x, this.y);
    };
    ;
    return PointedClass2;
}());
exports.PointedClass2 = PointedClass2;
;
