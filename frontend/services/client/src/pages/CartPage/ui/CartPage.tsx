import { FC } from 'react';
import { classNames } from 'shared/lib/classNames/classNames';
import { useTranslation } from 'next-i18next';

interface CartPageProps {
    className?: string;
}

const CartPage: FC<CartPageProps> = (props) => {
    const { className } = props;
    const { t } = useTranslation();

    return (
        <div className={classNames('', {}, [className])}>
            {t('CartPage')}
        </div>
    );
};

export default CartPage;
