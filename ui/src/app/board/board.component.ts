import {Component, OnInit, ViewEncapsulation} from '@angular/core';

import {PlayApiService} from '../play-api.service';
import {Subscription} from 'rxjs';
import {BoardModel} from '../board.model';
import {CellModel} from '../cell.model';


@Component({
    selector: 'app-board',
    providers: [PlayApiService],
    templateUrl: './board.component.html',
    styleUrls: ['./board.component.css'],
    encapsulation: ViewEncapsulation.None
})
export class BoardComponent implements OnInit {
    game: Subscription;
    board: BoardModel;


    constructor(private playService: PlayApiService) {
    }

    ngOnInit() {

        this.game = this.playService.startGame().subscribe(res => {
                this.board = res;
            },
            console.error);

    }

    //
    // sendBoard(selection: PlayModel) {
    //   if (!selection) {return;}
    //   this.playService.startGame()
    // }
    //
    onClick(selectedCell: CellModel) {
        if (selectedCell.value === '___') {
            selectedCell.value = 'O';
        }
    }
}
