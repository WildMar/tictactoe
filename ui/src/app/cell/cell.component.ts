import {Component, EventEmitter, Input, OnInit, Output} from '@angular/core';
import {Cell} from "../cell";


@Component({
  selector: 'app-cell',
  templateUrl: './cell.component.html',
  styleUrls: ['./cell.component.css'],

})
export class CellComponent implements OnInit {
  @Input() value;
  @Output("userClick") click = new EventEmitter<string>();



  constructor() {
  }

  ngOnInit() {
  }

  cellClick() {
    this.click.emit("")
  }
}
