var PointedClass = /** @class */ (function () {
    function PointedClass(x, y) {
        this.x = x;
        this.y = y;
    }
    PointedClass.prototype.draw = function () {
        console.log('drawing x and y', this.x, this.y);
    };
    ;
    return PointedClass;
}());
;
var pointObject = new PointedClass(2, 4);
pointObject.draw();
