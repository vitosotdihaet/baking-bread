import { FC, memo } from 'react';
import {
    GoodList,
    GoodTypeItem,
    type GoodTypeWithGoods,
} from 'entities/Good';
import { classNames } from 'shared/lib/classNames/classNames';
import { Divider } from 'shared/ui/Divider/Divider';
import { Column } from 'shared/ui/Stack';

interface GoodListWithTypeProps {
    className?: string;
    goodType: GoodTypeWithGoods;
}

export const GoodListWithType: FC<GoodListWithTypeProps> = memo((props: GoodListWithTypeProps) => {
    const { className, goodType } = props;

    if (goodType.goods.length === 0) {
        return null;
    }

    return (
        <>
            <Column
                gap='16'
                className={classNames('', {}, [className])}
            >
                <GoodTypeItem goodType={goodType} />
                <GoodList goods={goodType.goods} />
            </Column>
            <Divider />
        </>
    );
});
