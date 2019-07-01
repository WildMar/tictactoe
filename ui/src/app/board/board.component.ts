import {Component, OnInit, ViewEncapsulation} from '@angular/core';



@Component({
  selector: 'app-board',
  templateUrl: './board.component.html',
  styleUrls: ['./board.component.css'],
  encapsulation: ViewEncapsulation.None
})
export class BoardComponent implements OnInit {
  cells: string[] = [];

  constructor() {
  }

  ngOnInit() {
    for (let i = 0; i < 9; i++) {
      this.cells[i] = "";
    }
  }
}
