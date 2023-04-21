import { useTranslation } from 'next-i18next';
import { memo } from 'react';
import { classNames } from 'shared/lib/classNames/classNames';
import cls from './CartPage.module.scss';

interface CartPageProps {
    className?: string;
}

const CartPage = memo((props: CartPageProps) => {
    const { className } = props;
    const { t } = useTranslation();

    return (
        <div className={classNames(cls.CartPage, {}, [className])}>
            {t('Cart Page')}
        </div>
    );
});

export default CartPage;
