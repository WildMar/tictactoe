import {DeserializableModel} from './deserializable.model';
import {CellModel} from './cell.model';

export class BoardModel implements DeserializableModel {
    public cells: CellModel[];
    public moveNumber: number;

    deserialize(input: any): this {
        Object.assign(this, input);
        this.cells = input.cells.map(cell => new CellModel().deserialize(cell));
        return this;
    }

    getBoard() {
        return this.cells;
    }

}