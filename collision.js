
function checkCol(ele1, ele2){
	const rect1 = ele1.getBoundingClientRect();
	const rect2 = ele2.getBoundingClientRect();

	return !(rect1.right < rect2.left || rect1.left > rect2.right || rect1.bottom < rect2.top || rect1.top > rect2.bottom);
}


function collisionTest(rect, tiles){
	const hitlist = [];
	for(let tile of tiles){
		if (checkCol(tile, rect)){
			hitlist.push(tile)
		}
	}
	return hitlist;
}


