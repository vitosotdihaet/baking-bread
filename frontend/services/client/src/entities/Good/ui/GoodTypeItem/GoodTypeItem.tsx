import { FC, memo } from 'react';
import { Column } from 'shared/ui/Stack';
import { Typography } from 'shared/ui/Typography/Typography';
import { GoodType, GoodTypeWithGoods } from '../../model/types/goods';

interface GoodTypeProps {
    className?: string;
    goodType: GoodType | GoodTypeWithGoods;
}

export const GoodTypeItem: FC<GoodTypeProps> = memo((props: GoodTypeProps) => {
    const {
        className,
        goodType,
    } = props;

    return (
        <Column gap='8' className={className}>
            <Typography
                id={goodType.name}
                size='xl'
                family='sans'
                title={goodType.name}
            />
            <Typography
                size='md'
            >
                {goodType.description}
            </Typography>
        </Column>
    );
});
