import {Component, OnInit, ViewEncapsulation} from '@angular/core';
import {Cell} from "../cell";
import {PlayApiService} from "../play-api.service";
import {Subscription} from "rxjs";
import {PlayModel} from "../play.model";


@Component({
  selector: 'app-board',
  providers: [PlayApiService],
  templateUrl: './board.component.html',
  styleUrls: ['./board.component.css'],
  encapsulation: ViewEncapsulation.None
})
export class BoardComponent implements OnInit {
  cells: Cell[] = [];
  game: Subscription;
  board: PlayModel;


  constructor(private playService: PlayApiService) {
  }

  ngOnInit() {

    this.game = this.playService.startGame().subscribe(res => {
      this.board = res;
    },
    console.error);

    // TODO: Make this better when you have time
    this.cells[0] = {value: this.board["row1"][0]};
    this.cells[1] = {value: this.board["row1"][1]};
    this.cells[2] = {value: this.board["row1"][2]};
    this.cells[0] = {value: this.board["row2"][0]};
    this.cells[1] = {value: this.board["row2"][1]};
    this.cells[2] = {value: this.board["row2"][2]};
    this.cells[0] = {value: this.board["row3"][0]};
    this.cells[1] = {value: this.board["row3"][1]};
    this.cells[2] = {value: this.board["row3"][2]};

  }

  sendBoard(selection: PlayModel) {
    if (!selection) {return;}
    this.playService.startGame()
  }

  onClick(selectedCell: Cell) {
    if (selectedCell.value == "___") {
      selectedCell.value = "O";
    }
  }
}
