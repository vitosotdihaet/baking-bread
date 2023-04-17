import Image from 'next/image';
import { useTranslation } from 'next-i18next';
import { FC, memo } from 'react';
import { classNames } from 'shared/lib/classNames/classNames';
import { Button } from 'shared/ui/Button/Button';
import { Row } from 'shared/ui/Stack';
import { Typography } from 'shared/ui/Typography/Typography';
import { unAvailableGoodLabels } from '../../consts/unavaliableGoods';
import { Good } from '../../model/types/goods';
import cls from './GoodCard.module.scss';

interface GoodCardProps {
    className?: string;
    good: Good;
}

export const GoodCard: FC<GoodCardProps> = memo((props: GoodCardProps) => {
    const {
        className,
        good,
    } = props;
    const { t } = useTranslation();

    const renderBuyGoodButton = (good: Good) => {
        // Flags
        const isGoodAvailable = good.available;
        const isNotOnlyOne = isGoodAvailable && good.quantity > 1;

        // Labels
        const quantityLabel = `/ ${good.quantity} ${t('pcs')}`;
        const buttonLabel = `${t('Add to Cart')} $${good.price}.99`;

        return (
            <Button
                after={isNotOnlyOne && quantityLabel}
                disabled={!isGoodAvailable}
            >
                {
                    t(`${isGoodAvailable
                        ? buttonLabel
                        : unAvailableGoodLabels[good.id % 2]}`)
                }
            </Button>
        );
    };

    return (
        <div className={classNames(cls.GoodCard, {}, [className])}>
            <Row gap='12'>
                <div className={cls.image}>
                    <Image
                        width={1920}
                        height={128}
                        src={good.image}
                        alt={good.name}
                    />
                </div>
                <div>
                    <Row gap='4' align='center'>
                        <Typography
                            title={good.name}
                            family='sans'
                            size='lg'
                        />
                        <Typography
                            color='disabled'
                            size='sm'
                        >
                            {t(`${good.weight}g`)}
                        </Typography>
                    </Row>
                    <Typography
                        color='secondary'
                        size='sm'
                    >
                        {good.description}
                    </Typography>
                </div>
            </Row>
            {renderBuyGoodButton(good)}
        </div>
    );
});
