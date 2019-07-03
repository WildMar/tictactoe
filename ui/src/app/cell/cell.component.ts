import {Component, EventEmitter, Input, OnInit, Output} from '@angular/core';
import {CellModel} from "../cell.model";


@Component({
  selector: 'app-cell',
  templateUrl: './cell.component.html',
  styleUrls: ['./cell.component.css'],

})
export class CellComponent implements OnInit {
  @Input() value;
  @Output('userClick') click = new EventEmitter<string>();



  constructor() {
  }

  ngOnInit() {
  }

  cellClick() {
    this.click.emit('');
  }
}
