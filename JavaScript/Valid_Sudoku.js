/**
 * @param {character[][]} board
 * @return {boolean}
 */
var isValidSudoku = function(board) {
    let cols = new Array(9).fill().map(() => new Set());
    let rows = new Array(9).fill().map(() => new Set());
    let squares = new Array(33).fill().map(() => new Set());
    for (let r=0;r<9;r++){
        for(let c=0;c<9;c++){
            let num = board[r][c];
            if(num=="."){
                continue;
            }
            if (rows[r].has(num) || cols[c].has(num) || squares[Math.floor(r / 3) * 10 + Math.floor(c / 3)].has(num)) {
                return false;
            }
            rows[r].add(num);
            cols[c].add(num);
            squares[Math.floor(r / 3) * 10 + Math.floor(c / 3)].add(num);
        }
    }
    console.log(squares);
    return true;
};
