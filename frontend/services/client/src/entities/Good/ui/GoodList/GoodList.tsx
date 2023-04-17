import { FC, memo } from 'react';
import { classNames } from 'shared/lib/classNames/classNames';
import { Column } from 'shared/ui/Stack';
import { Good } from '../../model/types/goods';
import { GoodCard } from '../GoodCard/GoodCard';

interface GoodListProps {
    className?: string;
    goods: Good[]
}

export const GoodList: FC<GoodListProps> = memo((props: GoodListProps) => {
    const {
        className,
        goods,
    } = props;

    return (
        <Column gap='16' fullWidth className={classNames('', {}, [className])}>
            {goods.map((good) => (
                <GoodCard
                    key={good.id}
                    good={good}
                />
            ))}
        </Column>
    );
});
