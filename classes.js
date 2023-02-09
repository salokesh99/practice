var Pointed = /** @class */ (function () {
    function Pointed() {
    }
    Pointed.prototype.draw = function () {
        console.log('drawing x and y', this.x, this.y);
    };
    ;
    Pointed.prototype.drawDistance = function (another) {
        // ..
    };
    ;
    return Pointed;
}());
;
var point = new Pointed();
point.x = 2;
point.y = 4;
point.draw();
