import { ComponentStory, ComponentMeta } from '@storybook/react';
import { AppLink } from './AppLink';

export default {
    title: 'shared/AppLink',
    component: AppLink,
    args: {
        href: '/',
        children: 'AppLink',
    },
} as ComponentMeta<typeof AppLink>;

const Template: ComponentStory<typeof AppLink> = (args) => <AppLink {...args} />;

export const Primary = Template.bind({});
Primary.args = {
    variant: 'primary',
};

export const Secondary = Template.bind({});
Secondary.args = {
    variant: 'secondary',
};

export const Accent = Template.bind({});
Accent.args = {
    variant: 'accent',
};

export const Soft = Template.bind({});
Soft.args = {
    variant: 'soft',
};

export const Disabled = Template.bind({});
Disabled.args = {
    variant: 'disabled',
};

export const SizeXS = Template.bind({});
SizeXS.args = {
    size: 'xs',
};

export const SizeSM = Template.bind({});
SizeSM.args = {
    size: 'sm',
};

export const SizeMD = Template.bind({});
SizeMD.args = {
    size: 'md',
};

export const SizeLG = Template.bind({});
SizeLG.args = {
    size: 'lg',
};

export const SizeXL = Template.bind({});
SizeXL.args = {
    size: 'xl',
};
