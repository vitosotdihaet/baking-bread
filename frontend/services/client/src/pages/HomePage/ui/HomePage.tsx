import { FC } from 'react';
import { classNames } from 'shared/lib/classNames/classNames';
import { useTranslation } from 'next-i18next';

interface HomePageProps {
    className?: string;
}

const HomePage: FC<HomePageProps> = (props) => {
    const { className } = props;
    const { t } = useTranslation();

    return (
        <div className={classNames('', {}, [className])}>
            {t('HomePage')}
        </div>
    );
};

export default HomePage;
