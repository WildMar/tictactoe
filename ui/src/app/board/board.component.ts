import {Component, OnInit, ViewEncapsulation} from '@angular/core';
import {Cell} from "../cell";


@Component({
  selector: 'app-board',
  templateUrl: './board.component.html',
  styleUrls: ['./board.component.css'],
  encapsulation: ViewEncapsulation.None
})
export class BoardComponent implements OnInit {
  cells: Cell[] = [];

  constructor() {
  }

  ngOnInit() {
    for (let i = 0; i < 9; i++) {
      this.cells[i] = {value:"___"};
    }
  }

  onClick(selectedCell: Cell) {
    if (selectedCell.value == "___") {
      selectedCell.value = "O";
    }
  }
}
